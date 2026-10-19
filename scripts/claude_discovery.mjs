// Initialization only: the held input never yields a user message or model turn.
import fs from "node:fs";
import { pathToFileURL } from "node:url";

const input = JSON.parse(fs.readFileSync(process.argv[2], "utf8"));
const { query } = await import(pathToFileURL(input.sdk).href);
let release;
const held = new Promise(resolve => { release = resolve; });
async function* emptyInput() { await held; }
const session = query({
  prompt: emptyInput(),
  options: {
    cwd: input.project,
    env: process.env,
    pathToClaudeCodeExecutable: input.executable,
    settingSources: ["project"],
    persistSession: false,
  },
});
const timer = setTimeout(() => { session.close(); release(); }, 25000);
try {
  await session.initializationResult();
  const commands = await session.supportedCommands();
  console.log(JSON.stringify({names: commands.filter(c => c.name.startsWith("aw-")).map(c => c.name).sort()}));
} finally {
  clearTimeout(timer);
  session.close();
  release();
}
