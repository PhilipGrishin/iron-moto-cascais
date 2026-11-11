const fs = require('fs');
const path = require('path');

const BUILD_DIR = __dirname;
const SITE_ROOT = path.resolve(BUILD_DIR, '..', '..');
const content = fs.readFileSync(path.join(SITE_ROOT, 'assets', 'main.js'), 'utf8');

// Find I18N block by content marker — robust against other additions earlier in file.
const startMarker = 'const I18N = {';
const startIdx = content.indexOf(startMarker);
if (startIdx === -1) {
  console.error('Could not find "const I18N = {" in main.js');
  process.exit(1);
}

// Walk forward to find the matching closing brace (skip braces inside strings)
let depth = 0;
let i = startIdx + 'const I18N = '.length; // position at the first '{'
let inString = null;
let escape = false;
for (; i < content.length; i++) {
  const c = content[i];
  if (escape) { escape = false; continue; }
  if (inString) {
    if (c === '\\') { escape = true; continue; }
    if (c === inString) inString = null;
    continue;
  }
  if (c === '"' || c === "'") { inString = c; continue; }
  if (c === '{') depth++;
  else if (c === '}') {
    depth--;
    if (depth === 0) { i++; break; }
  }
}
const literal = content.slice(startIdx + 'const I18N = '.length, i);
const I18N = eval('(' + literal + ')');
// Registry-owned stage labels also serve static chrome in every language.
const { execFileSync } = require('child_process');
const stage = JSON.parse(execFileSync(process.env.PYTHON || 'python3', ['-c',
  "import sys,json;sys.path.insert(0,sys.argv[1]);from stage_pages_data import STAGE_I18N;print(json.dumps(STAGE_I18N))", BUILD_DIR], {encoding:'utf8'}));
for (const lang of Object.keys(I18N)) Object.assign(I18N[lang], stage[lang]);

fs.writeFileSync(path.join(BUILD_DIR, 'i18n.json'), JSON.stringify(I18N, null, 2));
console.log('Saved i18n.json with languages:', Object.keys(I18N).join(', '));
for (const lang of Object.keys(I18N)) {
  console.log(`  ${lang}: ${Object.keys(I18N[lang]).length} keys`);
}
