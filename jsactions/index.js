const core = require('@actions/core');
const github = require('@actions/github');
const { execSync } = require('child_process');
const path = require('path');


try {

const getValue = core.getInput('who-to-greet');
const path_to_script = path.join(__dirname, 'scripts', 'pythonscript.py');

// Execute the Python script with the input value using the shell command
const getScriptResult = execSync(`python ${path_to_script} ${getValue}`).toString().trim();
console.log('Result of Python script:', getScriptResult);
core.setOutput("scriptresult", getScriptResult);
process.exit(0); // Exit with success status code

} catch (error) {
  core.setFailed(error.message);
}
