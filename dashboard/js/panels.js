export const missing = 'Not documented';
export const names = {
  converted: 'Converted THT',
  original: 'Original THT',
  planned: 'Planned THT',
  retained: 'Retained SMD',
  unresolved: 'Unresolved',
  excluded: 'Non-populated feature',
  removed: 'Removed package'
};
export const colors = {
  converted: '#85d999',
  original: '#80aed3',
  planned: '#dfb569',
  retained: '#df8d84',
  unresolved: '#acb4b2',
  excluded: '#818d83',
  removed: '#c0aabe'
};
export const esc = v => String(v ?? missing).replace(/[&<>"']/g, c => ({
  '&': '&amp;',
  '<': '&lt;',
  '>': '&gt;',
  '"': '&quot;',
  "'": '&#39;'
} [c]));
const chip = status => '<span class="chip" style="--tone:' + colors[status] + '"><i class="swatch"></i>' + esc(names[status] || status) + '</span>';
const facts = rows => '<dl class="facts">' + rows.map(([a, b]) => '<dt>' + esc(a) + '</dt><dd>' + esc(b) + '</dd>').join('') + '</dl>';
const field = (name, value) => '<div class="field"><span class="label">' + esc(name) + '</span><code>' + esc(value || missing) + '</code></div>';
const block = (title, content) => '<section class="ins-block"><h3>' + esc(title) + '</h3>' + content + '</section>';
const details = (title, content) => '<details class="detail ins-block"><summary>' + esc(title) + '</summary>' + content + '</details>';
const card = (title, html) => '<article class="panel report-card"><h3>' + esc(title) + '</h3>' + html + '</article>';
const linkNames = {
  'audit/component-plan.csv': 'Baseline component plan',
  'audit/rev62/bplus-components.csv': 'Scenario B+ package plan',
  'audit/rev62/termination-crosswalk.csv': 'Termination crosswalk',
  'audit/implementation/slots/verification.json': 'Motherboard verification',
  'audit/implementation/slots/kicad-reports.zip': 'Raw ERC and DRC reports',
  '2000EATX-KiCAD-R31/2000ATX.kicad_pcb': 'Motherboard KiCad source',
  'audit/baseline/schematic.xml': 'Baseline schematic netlist',
  'SCENARIO_B_PLUS_IMPLEMENTATION.md': 'Implementation review',
  'ORIGINAL_A2000_REV62_COMPARISON.md': 'Rev 6.2 historical comparison',
  'coupon/CONNECTOR_RESOLUTION.md': 'TE connector resolution',
  'coupon/FABRICATION_READINESS.md': 'Coupon fabrication readiness'
};
export function source(path, p) {
  const url = 'https://github.com/GregWinfield/Amiga-2000-EATX/blob/' + encodeURIComponent(p.commit) + '/' + path.split('/').map(encodeURIComponent).join('/');
  return '<a class="doc-link" target="_blank" rel="noopener" href="' + url + '">' + esc(linkNames[path] || path) + '</a>';
}
export function metrics(d) {
  const {
    stats: s
  } = d;
  const cells = [
    ['Current through-hole', s.current.percent + '%', '', s.current.tht + ' of ' + s.current.total + ' packages', 'board'],
    ['Completed conversions', s.status.converted, '', 'SMD to through-hole', 'check'],
    ['Planned conversions', s.status.planned, '', 'Remaining component positions', 'layers'],
    ['Proposed THT target', s.target.percent + '%', '', s.target.tht + ' of ' + s.target.total + ' target packages', 'target']
  ];
  return cells.map(([title, val, unit, foot, ic]) => '<article class="metric"><div class="metric-top">' + esc(title) + '<span data-icon="' + ic + '"></span></div><div class="stat-value">' + esc(val) + '<small>' + esc(unit) + '</small></div><div class="metric-foot">' + esc(foot) + '</div></article>').join('');
}
export function inspector(r, d, boards) {
  const p = d.provenance;
  const f = boards.current.footprints.find(f => f.ref === r.currentRefs[0]);
  const coords = f ? f.xy.map(n => Number(n.toFixed(3))).join(', ') + ' mm' : missing;
  const changed = r.change.length ? r.change.join(', ') : 'No package change';
  let html = '<div class="ins-block"><div class="ins-title"><h3 class="ref" style="font-size:1.8rem;margin:0">' + esc(r.ref) + '</h3><span class="value-tag">' + esc(r.value) + '</span></div>' + chip(r.status) + '<p>' + esc(r.category) + ' · ' + esc(r.sheet) + '</p><button id="focus-component" class="focus-button"><span data-icon="target"></span>Zoom to component</button></div>';
  html += block('Package comparison', field('Original · ' + r.originalMount, r.originalFootprint) + field('Current · ' + r.currentMount, r.currentFootprint) + (r.proposedFootprint !== r.currentFootprint ? field('Proposed', r.proposedFootprint) : '') + field('Change', changed));
  html += block('Engineering state', facts([
    ['Implementation', r.implemented],
    ['Electrical', r.electrical],
    ['Mechanical', r.mechanical],
    ['Fabrication', r.fabrication],
    ['Physical validation', r.physical]
  ]));
  html += details('Placement and function', '<p>' + esc(r.description) + '</p>' + field('Footprint origin', coords) + field('Side / rotation', f ? f.side + ' / ' + f.angle + '°' : missing) + field('Source references', r.originalRefs.join(', ')) + field('Current references', r.currentRefs.join(', ')));
  html += details('Nets · ' + r.nets.length, '<div class="nets">' + (r.nets.map(n => '<code>' + esc(n) + '</code>').join('') || missing) + '</div>');
  if (r.branches.length) {
    const g = d.groups.find(g => g.ref === r.group);
    const group = g ? '<p>' + esc((g.implemented ? 'Implemented' : 'Planned') + ' package ' + g.ref + ' · ' + g.members.join(', ')) + '</p>' : '';
    const resistance = value => value ? esc(value) + ' Ω' : missing;
    html += details('Termination branches · ' + r.branches.length, group + '<ul class="branch-list">' + r.branches.map(b => '<li><b>' + esc(b.eatx_signal) + '</b> · ' + esc(b.eatx_contact) + '<br>' + esc(b.eatx_cap) + ' → ' + esc(b.eatx_private) + ' → ' + esc(b.eatx_element) + '<br>Scenario B+ ' + esc(b.bplus_element) + ' · ' + esc(b.return_net) + '<br>Factory ' + esc(b.historical_element) + ' (Rev 6.0 parts list) · ' + resistance(b.rev60_ohms) + '<br>Rev 6.2 reconstruction · ' + resistance(b.reconstruction_ohms) + '<br>EATX · ' + resistance(b.eatx_ohms) + '</li>').join('') + '</ul>');
  }
  html += details('Historical comparison', r.history.map(h => '<div class="field"><b>' + esc(h.ref) + '</b><span>' + esc(h.package) + '</span><p>' + esc(h.function) + '</p><p>' + esc(h.evidence) + '</p>' + source(h.source, p) + '</div>').join('') || missing);
  html += details('Notes and risks', '<p>' + esc(r.notes) + '</p>' + r.risks.map(n => '<p>' + esc(n) + '</p>').join(''));
  return html + details('Source documents', r.sources.map(n => source(n, p)).join(''));
}
export function registerRows(rows) {
  return rows.map(r => '<tr><td><button class="table-ref" data-ref="' + esc(r.ref) + '">' + esc(r.ref) + '</button></td><td>' + esc(r.value) + '</td><td>' + esc(r.category) + '</td><td>' + chip(r.status) + '</td><td><code>' + esc(r.currentFootprint) + '</code></td><td>' + esc(r.change.join(', ') || '—') + '</td></tr>').join('') || '<tr><td colspan="6">No matching components.</td></tr>';
}
export function progress(d) {
  const s = d.stats;
  const row = (name, n, max, text) => '<div class="chart-row"><span>' + esc(name) + '</span><div class="bar"><i style="width:' + 100 * n / max + '%"></i></div><span class="mono">' + esc(text) + '</span></div>';
  return '<h2>Package population</h2><div class="report-grid"><div><h3>Through-hole share</h3>' + [
    ['Original', s.original],
    ['Current', s.current],
    ['Proposed', s.target]
  ].map(([name, g]) => row(name, g.tht, g.total, g.percent + '%')).join('') + '</div><div>' + facts([
    ['Original SMD / THT', s.original.smd + ' / ' + s.original.tht],
    ['Current SMD / THT', s.current.smd + ' / ' + s.current.tht],
    ['Retained SMD', s.status.retained],
    ['Unresolved', s.status.unresolved],
    ['Excluded board features', s.excluded]
  ]) + '</div></div><div class="table-scroll"><table><thead><tr><th>Component type</th><th>Original</th><th>Current</th><th>Current THT</th><th>Converted</th><th>Planned positions</th><th>Target packages</th></tr></thead><tbody>' + s.categories.map(c => '<tr>' + [c.name, c.original, c.current, c.currentTht, c.converted, c.planned, c.target].map(x => '<td>' + esc(x) + '</td>').join('') + '</tr>').join('') + '</tbody></table></div><p>Counts cover design positions, including assembly options. Target packages count each proposed SIP body once.</p>';
}
export function verification(d, board) {
  const v = d.verification,
    p = d.provenance,
    fmt = n => n?.toLocaleString() ?? missing;
  const cv = (n) => v.currentEvidence ? n : 'Earlier snapshot · ' + n;
  let h = '<div class="report-grid">' + card('Design source', facts([
    ['Source branch', p.branch],
    ['Source commit', p.commit],
    ['PCB revision', board.titleBlock.revision || missing],
    ['PCB file format', board.pcbFileFormat],
    ['Exported with', 'KiCad ' + p.kicad],
    ['Generated (UTC)', p.generated]
  ]));
  h += card('Electrical checks', facts([
    ['ERC errors / warnings', cv(v.erc.error + ' / ' + fmt(v.erc.warning))],
    ['DRC errors / warnings', cv(v.drcErrors + ' / ' + v.drcWarnings)],
    ['Refilled baseline DRC', v.controlDrcErrors + ' / ' + v.controlDrcWarnings],
    ['Unrouted connections', cv(v.unrouted)],
    ['Schematic-field parity findings', cv(v.parity_findings)],
    ['Physical pad-net changes', cv(v.pad_net_changes)],
    ['Compared schematic pins / nets', fmt(v.schematic_pin_assignments) + ' / ' + v.nets]
  ]));
  h += card('Mechanical and release status', facts([
    ['Outline', cv(v.edge_geometry_changed ? 'Changed' : 'Matches baseline')],
    ['Mounting centres', cv(v.fixed_mounts.length + ' checked')],
    ['Four-layer stack', cv(v.stackup_changed ? 'Changed' : 'Matches baseline')],
    ['TE socket geometry', v.currentEvidence && v.all_five_TE_socket_padstacks_checked ? 'Provisionally approved for layout' : 'Review required'],
    ['Fabrication', 'Awaiting supplier acceptance'],
    ['Physical fit and electrical tests', 'Outstanding']
  ])) + '</div>';
  h += '<section class="panel report-panel"><h2>Verification differences</h2><p>KiCad count comparisons use the same-tool refilled control. The item-level comparison records which findings appeared or disappeared.</p><div class="table-scroll"><table><thead><tr><th>DRC rule</th><th>Control</th><th>Current report</th></tr></thead><tbody>' + [...new Set([...Object.keys(v.drc), ...Object.keys(v.same_tool_control_drc)])].map(k => '<tr><td>' + esc(k.replaceAll('_', ' ')) + '</td><td>' + esc(v.same_tool_control_drc[k] || 0) + '</td><td>' + esc(v.drc[k] || 0) + '</td></tr>').join('') + '</tbody></table></div>';
  for (const [k, ls] of Object.entries(v.drc_item_deltas)) h += '<details class="detail"><summary>' + esc(k === 'appeared' ? 'Appeared in report' : 'Absent from report') + ' · ' + ls.length + '</summary><ul class="branch-list">' + ls.map(e => '<li>' + esc(e.description) + ' · ' + esc(e.items.join(' / ')) + '</li>').join('') + '</ul></details>';
  h += '<p>The linked reports identify the inherited findings and the objects involved in each change.</p></section>';
  h += '<section class="panel report-panel"><h2>Engineering risks</h2><div class="table-scroll"><table><thead><tr><th>Item</th><th>Consequence</th><th>Outstanding validation</th></tr></thead><tbody>' + v.risks.map(r => '<tr><td>' + esc(r.risk) + '</td><td>' + esc(r.consequence) + '</td><td>' + esc(r.action) + '</td></tr>').join('') + '</tbody></table></div></section>';
  return h + '<section class="panel report-panel"><h2>Evidence</h2>' + v.sources.map(path => source(path, p)).join('') + '</section>';
}
