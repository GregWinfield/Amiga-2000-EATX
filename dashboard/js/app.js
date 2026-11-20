import {
  Viewer,
  layerNames
} from './viewer.js';
import {
  names,
  colors,
  esc,
  metrics,
  inspector,
  registerRows,
  progress,
  verification
} from './panels.js';
const $ = id => document.getElementById(id);
const icons = {
  board: 'M3 3h14v14H3z M6 7h4v4h4 M6 14h2 M13 6h1',
  check: 'M3 10l4 4L17 4',
  layers: 'M2 7l8-4 8 4-8 4z M2 11l8 4 8-4 M2 15l8 4 8-4',
  target: 'M10 1v3 M10 16v3 M1 10h3 M16 10h3 M10 4a6 6 0 1 0 .01 0',
  inspect: 'M2 3h16v14H2z M12 3v14 M4.5 6h5 M4.5 9h3',
  compare: 'M2 4h7v12H2z M12 4h6v12h-6z',
  search: 'M8 2a6 6 0 1 0 .01 0 M12.5 12.5l5 5',
  fit: 'M3 7V3h4 M13 3h4v4 M17 13v4h-4 M7 17H3v-4',
  reset: 'M3 8a7 7 0 1 1 1 7 M3 3v5h5'
};

function hydrate(root = document) {
  for (const el of root.querySelectorAll('[data-icon]')) el.innerHTML = '<svg class="icon" aria-hidden="true" viewBox="0 0 20 20"><path d="' + icons[el.dataset.icon] + '"/></svg>';
}

function option(value, label) {
  const o = document.createElement('option');
  o.value = value;
  o.textContent = label;
  return o;
}
async function fetchJSON(url) {
  const res = await fetch(url);
  if (!res.ok) throw Error(res.status + ' ' + url);
  return res.json();
}
async function run() {
  const [data, current, original] = await Promise.all(['./data/manifest.json', './data/current/board.json', './data/original/board.json'].map(fetchJSON));
  if (data.provenance.schema !== 1 || !current.footprints.length || !original.footprints.length) throw Error('Missing or incompatible engineering snapshot');
  const boards = {
    current,
    original
  };
  const rows = data.components,
    byRef = new Map(rows.map(r => [r.ref, r]));
  let selected, page = 'board';
  const m = data.provenance,
    s = data.stats;
  $('metrics').innerHTML = metrics(data);
  $('source-id').textContent = m.branch + ' / ' + m.commit.slice(0, 8);
  $('board-size').textContent = current.bounds.slice(2).map(v => v.toFixed(1)).join(' × ') + ' mm';
  $('snapshot-label').title = 'Snapshot generated ' + m.generated;
  if (data.warnings.length) {
    $('notice').hidden = false;
    $('notice').textContent = data.warnings.join(' ');
  }

  function select(r, focus) {
    if (!r) return;
    selected = r;
    viewer.setSelected(r, focus);
    $('inspector').innerHTML = inspector(r, data, boards);
    $('inspector').scrollTop = 0;
    $('focus-component').onclick = () => viewer.setSelected(selected, true);
    hydrate($('inspector'));
  }
  const viewer = new Viewer(boards, data, colors, select);
  for (const [key, label] of Object.entries(layerNames)) {
    const l = document.createElement('label'),
      c = document.createElement('input');
    c.type = 'checkbox';
    c.dataset.layer = key;
    c.checked = viewer.visible.has(key);
    c.disabled = !current.layers[key] && !original.layers[key] && !['labels', 'overlay'].includes(key);
    l.append(c, document.createTextNode(label + (c.disabled ? ' · unavailable' : '')));
    $('layer-list').append(l);
    c.onchange = () => viewer.setLayer(key, c.checked);
  }
  for (const r of data.regions) {
    const o = option(r.id, r.name + (r.bounds ? '' : ' · unclassified'));
    o.disabled = !r.bounds;
    o.title = r.basis;
    $('region').append(o);
  }
  $('region').onchange = () => {
    const r = data.regions.find(r => r.id === $('region').value);
    viewer.setRegion(r);
    $('region').title = r?.basis || 'Zoom to functional region';
  };
  for (const status of Object.keys(s.status)) {
    const b = document.createElement('button');
    b.dataset.status = status;
    b.style.setProperty('--tone', colors[status]);
    b.innerHTML = '<i class="swatch"></i>' + esc(names[status]);
    b.title = 'Filter board: ' + names[status] + ' (' + s.status[status] + ')';
    b.setAttribute('aria-pressed', 'false');
    b.onclick = () => {
      viewer.filter = viewer.filter === status ? '' : status;
      for (const e of $('legend').children) e.setAttribute('aria-pressed', e.dataset.status === viewer.filter);
      viewer.updateMarks();
    };
    $('legend').append(b);
  }

  function openSelection(r) {
    show('board');
    viewer.filter = '';
    for (const b of $('legend').children) b.setAttribute('aria-pressed', 'false');
    if (viewer.region && !viewer.region.refs.includes(r.ref)) {
      viewer.region = null;
      $('region').value = '';
    }
    if (!r.currentRefs.length && !viewer.comparing) compare(true);
    select(r, true);
    $('reference-list').hidden = true;
    $('search').value = r.ref;
  }

  function compare(on) {
    viewer.setCompare(on);
    $('compare').setAttribute('aria-pressed', on);
    $('compare').lastChild.textContent = on ? 'Exit comparison' : 'Compare revisions';
  }
  $('compare').onclick = () => compare(!viewer.comparing);
  const result = $('reference-list');

  function suggestions() {
    const q = $('search').value.trim().toUpperCase();
    result.replaceChildren();
    if (!q) {
      result.hidden = true;
      return;
    }
    const group = data.groups.find(g => g.ref.toUpperCase() === q);
    const hits = rows.filter(r => r.ref.toUpperCase().includes(q) || group?.members.includes(r.ref) ||
      r.originalRefs.some(a => a.toUpperCase() === q)).sort((a, b) => Number(b.ref.toUpperCase() === q) - Number(a.ref.toUpperCase() === q) || a.ref.localeCompare(b.ref, undefined, {
      numeric: true
    })).slice(0, 40);
    if (group) {
      const msg = document.createElement('p');
      msg.className = 'empty';
      msg.textContent = (group.implemented ? 'Placed' : 'Planned') + ' ' + group.ref + ' · ' + group.members.length + ' members';
      result.append(msg);
    }
    for (const r of hits) {
      const b = document.createElement('button');
      b.dataset.ref = r.ref;
      b.innerHTML = '<b>' + esc(r.ref) + '</b><small>' + esc(r.value) + '</small>';
      b.onclick = () => openSelection(r);
      result.append(b);
    }
    if (!hits.length) result.textContent = 'No matching reference.';
    result.hidden = false;
  }
  $('search').oninput = suggestions;
  $('search').onfocus = suggestions;
  $('search').onkeydown = e => {
    if (e.key === 'Enter') result.querySelector('button')?.click();
    if (e.key === 'Escape') result.hidden = true;
    if (e.key === 'ArrowDown') {
      e.preventDefault();
      result.querySelector('button')?.focus();
    }
  };
  document.addEventListener('click', e => {
    if (!e.target.closest('.search-wrap')) result.hidden = true;
    if (!e.target.closest('#layers')) $('layers').open = false;
  });
  document.addEventListener('keydown', e => {
    if (e.key === '/' && !['INPUT', 'SELECT', 'TEXTAREA'].includes(document.activeElement.tagName)) {
      e.preventDefault();
      show('board');
      $('search').focus();
      $('search').select();
    }
    if (e.key === 'Escape') {
      $('layers').open = false;
      result.hidden = true;
    }
  });

  function table() {
    const text = $('table-search').value.trim().toLowerCase();
    const visible = rows.filter(r => (!$('status-select').value || r.status === $('status-select').value) &&
      (!$('category-select').value || r.category === $('category-select').value) && (!$('changes-only').checked || r.change.length) &&
      (!text || [r.ref, r.value, r.currentFootprint, r.proposedPackage, ...r.originalRefs].some(v => v?.toLowerCase().includes(text))));
    $('parts-table').tBodies[0].innerHTML = registerRows(visible);
    $('parts-count').textContent = visible.length + ' / ' + rows.length + ' records';
  }
  $('status-select').append(option('', 'All statuses'));
  for (const st of new Set(rows.map(r => r.status))) $('status-select').append(option(st, names[st]));
  $('category-select').append(option('', 'All component types'));
  for (const n of [...new Set(rows.map(r => r.category))].sort()) $('category-select').append(option(n, n));
  for (const k of ['table-search', 'status-select', 'category-select', 'changes-only']) $(k).addEventListener('input', table);
  $('parts-table').onclick = e => {
    const ref = e.target.closest('button[data-ref]')?.dataset.ref;
    if (ref) openSelection(byRef.get(ref));
  };
  $('progress-panel').innerHTML = progress(data);
  $('verification-content').innerHTML = verification(data, current);
  const titles = {
    board: 'Board explorer',
    components: 'Component register',
    verification: 'Engineering verification'
  };

  function show(next) {
    if (!titles[next]) next = 'board';
    page = next;
    for (const k of Object.keys(titles)) $(k + '-page').hidden = k !== page;
    for (const b of document.querySelectorAll('[data-page]')) {
      b.classList.toggle('active', b.dataset.page === page);
      b.setAttribute('aria-current', b.dataset.page === page ? 'page' : 'false');
    }
    $('page-title').textContent = titles[page];
    $('compare').hidden = page !== 'board';
    if (page === 'components') table();
    if (location.hash !== '#' + page) history.replaceState(null, '', '#' + page);
  }
  for (const b of document.querySelectorAll('[data-page]')) b.onclick = () => show(b.dataset.page);
  window.addEventListener('hashchange', () => show(location.hash.slice(1)));
  select(rows.find(r => r.status === 'converted') || rows[0], false);
  show(location.hash.slice(1));
  hydrate();
}
hydrate();
run().catch(err => {
  const n = $('notice');
  n.hidden = false;
  n.textContent = 'Engineering snapshot failed to load. ' + err.message + '. Serve the dashboard over local HTTP and check the exported files.';
});
