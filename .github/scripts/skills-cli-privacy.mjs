import assert from 'node:assert/strict';
import { appendFileSync, readFileSync } from 'node:fs';

const catalog = JSON.parse(readFileSync(new URL('../../catalog.json', import.meta.url), 'utf8'));
const names = new Set(catalog.skills.map((skill) => skill.name));
const originalFetch = globalThis.fetch;
const record = (value) => appendFileSync(process.env.AW_SKILLS_EVENT_LOG, JSON.stringify(value) + '\n');

globalThis.fetch = async (input, init) => {
  const request = new Request(input, init);
  const url = new URL(request.url);
  if (!['skills.sh', 'www.skills.sh'].includes(url.hostname)) {
    assert(['api.github.com', 'github.com', 'raw.githubusercontent.com', 'codeload.github.com'].includes(url.hostname));
    assert(!url.username && !url.password && !request.headers.has('authorization') && !request.headers.has('cookie'));
    return originalFetch(input, init);
  }
  const fields = Object.fromEntries(url.searchParams);
  try {
    assert.equal(process.env.AW_REPORT_PUBLIC_INSTALL, 'true');
    assert.equal(process.env.GITHUB_ACTIONS, 'true');
    assert.equal(request.method, 'GET');
    assert(!request.headers.has('authorization') && !request.headers.has('cookie'));
    assert.equal(fields.source, 'suntianhu/agent-workflow-skills');
    assert(['/tele/t', '/tele/audit'].includes(url.pathname));
    const allowed = new Set(url.pathname === '/tele/t'
      ? ['v', 'event', 'source', 'skills', 'agents', 'skillFiles', 'ci']
      : ['source', 'skills']);
    assert(Object.keys(fields).every((key) => allowed.has(key)));
    assert(fields.skills.split(',').every((name) => names.has(name)));
    if (url.pathname === '/tele/t') {
      assert.equal(fields.event, 'install');
      assert.equal(fields.v, '1.7.4');
      assert.equal(fields.agents, 'codex');
      assert.equal(fields.ci, '1');
      const files = JSON.parse(fields.skillFiles);
      assert.deepEqual(Object.keys(files).sort(), fields.skills.split(',').sort());
      for (const [name, path] of Object.entries(files)) assert.equal(path, `skills/${name}/SKILL.md`);
    }
    record({ action: 'allowed', endpoint: url.pathname, fields });
  } catch (error) {
    record({ action: 'blocked', endpoint: url.pathname, fieldNames: Object.keys(fields) });
    throw error;
  }
  const response = await originalFetch(input, init);
  record({ action: 'response', endpoint: url.pathname, status: response.status });
  return response;
};
