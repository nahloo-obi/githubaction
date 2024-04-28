const core = require('@actions/core');
const github = require('@actions/github');
const { execSync } = require('child_process');
const path = require('path');


try {

(async () => {
const getBenchmarkValue = core.getInput('benchmark');
console.log('benchmark value:', getBenchmarkValue);

 // Run the Django application using the manage.py script
 const appCommand = 'python manage.py runserver 0.0.0.0:8000 &';
 execSync(appCommand);
 // Wait for a moment to ensure the Django app starts up
 await new Promise(resolve => setTimeout(resolve, 5000));


 // Get the process ID of the running Django application
 const pidCommand = 'pgrep -f \'python manage.py runserver\'';
 const pid = execSync(pidCommand).toString().trim();
 console.log('Result of Python script pid hereee:', pid);

 const path_to_script = path.join(__dirname, 'scripts', 'pythonscript.py');
 console.log('Result of Python script hereee:', path_to_script);

// Execute the Python script with the input value using the shell command
const getScriptResult = execSync(`python ${path_to_script} ${getBenchmarkValue}`).toString().trim();
//const getScriptResult = execSync(`python ${path_to_script} ${pid} ${getBenchmarkValue}`).toString().trim();

console.log('Result of Python script:', getScriptResult);

core.setOutput("performanceresult", getScriptResult);

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
