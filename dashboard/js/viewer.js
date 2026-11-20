const NS = 'http://www.w3.org/2000/svg';
const node = (tag, attrs = {}) => {
  const e = document.createElementNS(NS, tag);
  for (const [k, v] of Object.entries(attrs)) e.setAttribute(k, v);
  return e;
};
export const layerNames = {
  outline: 'Board outline',
  front: 'Top copper',
  back: 'Bottom copper',
  inner1: 'In1 · ground',
  inner2: 'In2 · power',
  silkF: 'Top silkscreen',
  silkB: 'Bottom silkscreen',
  fab: 'Top footprints',
  fabB: 'Bottom footprints',
  pads: 'Surface pad lands',
  vias: 'Vias',
  overlay: 'Conversion overlay',
  labels: 'Reference designators'
};
const physicalOrder = ['substrate', 'inner2', 'inner1', 'back', 'front', 'fabB', 'fab', 'vias', 'pads', 'silkB', 'silkF', 'outline'];
const byId = id => document.getElementById(id);

function union(boxes) {
  const x = Math.min(...boxes.map(b => b[0])),
    y = Math.min(...boxes.map(b => b[1]));
  return [x, y, Math.max(...boxes.map(b => b[0] + b[2])) - x, Math.max(...boxes.map(b => b[1] + b[3])) - y];
}
export class Viewer {
  constructor(boards, data, colors, select) {
    this.boards = boards;
    this.colors = colors;
    this.select = select;
    this.rows = new Map(data.components.map(r => [r.ref, r]));
    this.bySide = {
      original: new Map(),
      current: new Map()
    };
    for (const r of data.components)
      for (const side of ['original', 'current'])
        for (const ref of r[side + 'Refs']) this.bySide[side].set(ref, r);
    this.lookup = Object.fromEntries(Object.entries(boards).map(([s, b]) => [s, new Map(b.footprints.map(f => [f.ref, f]))]));
    this.full = union(Object.values(boards).map(b => b.bounds));
    this.visible = new Set(['substrate', 'outline', 'front', 'silkF', 'fab', 'pads', 'vias', 'overlay']);
    this.filter = '';
    this.region = null;
    this.comparing = false;
    this.selected = null;
    this.space = byId('workspace');
    this.fit();
    this.draw();
    byId('fit').onclick = () => this.fit();
    byId('reset').onclick = () => {
      this.setRegion(null);
      byId('region').value = '';
    };
    byId('zoom-in').onclick = () => this.zoom(1.4);
    byId('zoom-out').onclick = () => this.zoom(1 / 1.4);
    this.space.addEventListener('keydown', e => {
      const keys = {
        ArrowLeft: [-1, 0],
        ArrowRight: [1, 0],
        ArrowUp: [0, -1],
        ArrowDown: [0, 1]
      };
      if (keys[e.key]) {
        const [x, y] = keys[e.key];
        this.cam[0] += x * this.cam[2] / 10;
        this.cam[1] += y * this.cam[3] / 10;
        this.apply();
      } else if (e.key === 'Home') this.fit();
      else if (['+', '='].includes(e.key)) this.zoom(1.4);
      else if (e.key === '-') this.zoom(1 / 1.4);
      else return;
      e.preventDefault();
    });
  }
  fit() {
    this.frame(this.full, .075);
  }
  frame([x, y, w, h], margin = .18) {
    const [, , bw, bh] = this.full;
    const scale = Math.max(w / bw, h / bh, .025) * (1 + margin * 2);
    this.cam = [x + w / 2 - bw * scale / 2, y + h / 2 - bh * scale / 2, bw * scale, bh * scale];
    this.apply();
  }
  apply() {
    for (const s of this.space.querySelectorAll('.board')) s.setAttribute('viewBox', this.cam.join(' '));
    byId('zoom-level').textContent = Math.round(115 * this.full[2] / this.cam[2]) + '%';
  }
  zoom(mult, anchor) {
    const [x, y, w, h] = this.cam;
    const factor = Math.min(this.full[2] * 4 / w, Math.max(this.full[2] / 90 / w, 1 / mult));
    const [cx, cy] = anchor || [x + w / 2, y + h / 2];
    this.cam = [cx + (x - cx) * factor, cy + (y - cy) * factor, w * factor, h * factor];
    this.apply();
  }
  setRegion(region) {
    this.region = region;
    this.updateMarks();
    if (region?.bounds) this.frame(region.bounds, .06);
    else this.fit();
  }
  setSelected(row, focus = false) {
    this.selected = row;
    this.updateMarks();
    if (focus) {
      const boxes = [];
      for (const side of (this.comparing ? ['original', 'current'] : ['current', 'original'])) {
        for (const ref of row[side + 'Refs']) {
          const f = this.lookup[side].get(ref);
          if (f) boxes.push(f.bounds);
        }
        if (!this.comparing && boxes.length) break;
      }
      if (boxes.length) this.frame(union(boxes), .55);
    }
  }
  setCompare(value) {
    this.comparing = value;
    this.draw();
  }
  draw() {
    const panes = byId('panes');
    panes.replaceChildren();
    this.panes = [];
    for (const side of this.comparing ? ['original', 'current'] : ['current']) {
      const board = this.boards[side],
        [x, y, width, height] = board.bounds;
      const pane = document.createElement('div');
      pane.className = 'pane';
      panes.append(pane);
      const tag = document.createElement('span');
      tag.className = 'pane-label';
      tag.textContent = side === 'current' ? 'Scenario B+ · current' : 'Jason Beer · original R3.1';
      pane.append(tag);
      const svg = node('svg', {
        class: 'board',
        'aria-label': tag.textContent
      });
      pane.append(svg);
      const layers = {};
      for (const key of physicalOrder) {
        if (!board.layers[key]) continue;
        const img = node('image', {
          x,
          y,
          width,
          height,
          'data-art': key,
          'pointer-events': 'none',
          opacity: key === 'front' ? .32 : key === 'fab' ? .64 : 1
        });
        img.dataset.url = './data/' + side + '/' + board.layers[key];
        img.addEventListener('error', () => {
          const notice = byId('notice');
          notice.hidden = false;
          notice.textContent = 'Layer unavailable: ' + side + ' / ' + (layerNames[key] || key);
        });
        svg.append(img);
        layers[key] = img;
      }
      const marks = node('g'),
        labels = node('g', {
          'pointer-events': 'none'
        }),
        selected = node('g', {
          'pointer-events': 'none'
        });
      svg.append(marks, labels, selected);
      const items = [];
      const area = f => f.bounds[2] * f.bounds[3];
      for (const f of [...board.footprints].sort((a, b) => area(b) - area(a))) {
        const r = this.bySide[side].get(f.ref);
        if (!r) continue;
        const [px, py, w, h] = f.bounds;
        const hit = node('rect', {
          x: px,
          y: py,
          width: Math.max(w, .45),
          height: Math.max(h, .45),
          'data-ref': f.ref,
          'pointer-events': 'all',
          'vector-effect': 'non-scaling-stroke'
        });
        const label = node('text', {
          x: px + w / 2,
          y: py + h / 2,
          'text-anchor': 'middle',
          'font-size': 1.6,
          fill: '#fff',
          'paint-order': 'stroke',
          stroke: '#18291e',
          'stroke-width': .35
        });
        label.textContent = f.ref;
        marks.append(hit);
        labels.append(label);
        items.push({
          hit,
          label,
          r,
          f
        });
      }
      this.panes.push({
        side,
        svg,
        layers,
        items,
        selected
      });
      this.interact(svg, side);
    }
    this.apply();
    this.updateMarks();
  }
  setLayer(key, on) {
    if (on) this.visible.add(key);
    else this.visible.delete(key);
    this.updateMarks();
  }
  updateMarks() {
    for (const {
        side,
        layers,
        items,
        selected
      }
      of this.panes || []) {
      for (const [k, image] of Object.entries(layers)) {
        const visible = this.visible.has(k);
        image.style.display = visible ? '' : 'none';
        if (visible && !image.hasAttribute('href')) image.setAttribute('href', image.dataset.url);
      }
      selected.replaceChildren();
      for (const {
          hit,
          label,
          r,
          f
        }
        of items) {
        const match = (!this.filter || r.status === this.filter) && (!this.region || this.region.refs.includes(r.ref));
        const overlay = this.visible.has('overlay') && match && r.status !== 'excluded';
        const changed = this.comparing && r.change.length > 0 && match;
        hit.setAttribute('fill', overlay ? this.colors[r.status] || '#adb7b0' : 'transparent');
        hit.setAttribute('fill-opacity', overlay ? (this.filter ? .55 : .17) : 0);
        hit.setAttribute('stroke', changed ? '#ecf2da' : overlay ? this.colors[r.status] : 'none');
        hit.setAttribute('stroke-width', changed ? 1.4 : .53);
        hit.setAttribute('stroke-opacity', changed ? 1 : .75);
        if (changed) hit.setAttribute('stroke-dasharray', '3 2');
        else hit.removeAttribute('stroke-dasharray');
        hit.style.pointerEvents = match ? 'all' : 'none';
        label.style.display = this.visible.has('labels') && match ? '' : 'none';
        if (!match || r.ref !== this.selected?.ref) continue;
        const [x, y, w, h] = f.bounds;
        selected.append(node('rect', {
          x: x - .5,
          y: y - .5,
          width: w + 1,
          height: h + 1,
          fill: 'none',
          stroke: '#efffdc',
          'stroke-width': 2,
          'vector-effect': 'non-scaling-stroke'
        }));
        const t = node('text', {
          x: x + w / 2,
          y: y - .95,
          fill: '#faffee',
          'font-size': 2.6,
          'font-family': 'monospace',
          'text-anchor': 'middle',
          'paint-order': 'stroke',
          stroke: '#18291e',
          'stroke-width': .7
        });
        t.textContent = f.ref;
        selected.append(t);
      }
    }
    byId('view-mode').textContent = this.comparing ? 'Dashed outline · changed package' : this.region?.name || 'Component side';
  }
  interact(svg, side) {
    const pt = (x, y) => new DOMPoint(x, y).matrixTransform(svg.getScreenCTM().inverse());
    let start = null,
      drag = false;
    const tip = byId('hover-tip');
    svg.addEventListener('wheel', e => {
      e.preventDefault();
      const p = pt(e.clientX, e.clientY);
      this.zoom(Math.exp(-Math.sign(e.deltaY) * .16), [p.x, p.y]);
    }, {
      passive: false
    });
    svg.addEventListener('pointerdown', e => {
      if (e.button !== 0) return;
      start = {
        x: e.clientX,
        y: e.clientY,
        cam: [...this.cam],
        ref: e.target.dataset.ref
      };
      drag = false;
      svg.setPointerCapture(e.pointerId);
    });
    svg.addEventListener('pointermove', e => {
      const p = pt(e.clientX, e.clientY);
      byId('coordinate').textContent = 'X ' + p.x.toFixed(2) + '   Y ' + p.y.toFixed(2) + ' mm';
      if (start) {
        const dx = e.clientX - start.x,
          dy = e.clientY - start.y;
        if (Math.hypot(dx, dy) > 3) drag = true;
        if (drag) {
          tip.hidden = true;
          svg.classList.add('dragging');
          const scale = svg.getScreenCTM().a;
          this.cam = [start.cam[0] - dx / scale, start.cam[1] - dy / scale, ...start.cam.slice(2)];
          this.apply();
        }
        return;
      }
      const ref = e.target.dataset.ref;
      tip.hidden = !ref;
      if (ref) {
        tip.textContent = ref + ' · ' + this.lookup[side].get(ref).value;
        const b = this.space.getBoundingClientRect();
        tip.style.left = Math.max(0, Math.min(b.width - tip.offsetWidth - 4, e.clientX - b.left + 10)) + 'px';
        tip.style.top = Math.max(0, e.clientY - b.top - 33) + 'px';
      }
    });
    svg.addEventListener('pointerup', e => {
      if (!start) return;
      if (!drag && start.ref) this.select(this.bySide[side].get(start.ref), false);
      start = null;
      svg.classList.remove('dragging');
    });
    svg.addEventListener('pointercancel', () => {
      start = null;
      svg.classList.remove('dragging');
    });
    svg.addEventListener('pointerleave', () => {
      tip.hidden = true;
    });
  }
}
