const core = require('@actions/core');
const github = require('@actions/github');
const { execSync } = require('child_process');
const path = require('path');


try {

const getBenchmarkValue = core.getInput('benchmark');

 // Run the Django application using the manage.py script
 const appCommand = 'python manage.py runserver 0.0.0.0:8000 &';
 execSync(appCommand);

 (async () => {
 // Wait for a moment to ensure the Django app starts up
 await new Promise(resolve => setTimeout(resolve, 5000));


 // Get the process ID of the running Django application
 const pidCommand = 'pgrep -f \'python manage.py runserver\'';
 const pid = execSync(pidCommand).toString().trim();

 const path_to_script = path.join(__dirname, 'scripts', 'pythonscript.py');

// Execute the Python script with the input value using the shell command
const getScriptResult = execSync(`python ${path_to_script} ${pid} ${getBenchmarkValue}`).toString().trim();

console.log('Result of Python script:', getScriptResult);
core.setOutput("scriptresult", getScriptResult);

process.exit(0); // Exit with success status code
})();

} catch (error) {
  core.setFailed(error.message);
}



// try {

// const getValue = core.getInput('who-to-greet');
// const path_to_script = path.join(__dirname, 'scripts', 'pythonscript.py');

// // Execute the Python script with the input value using the shell command
// const getScriptResult = execSync(`python ${path_to_script} ${getValue}`).toString().trim();
// console.log('Result of Python script:', getScriptResult);
// core.setOutput("scriptresult", getScriptResult);
// process.exit(0); // Exit with success status code

// } catch (error) {
//   core.setFailed(error.message);
// }
