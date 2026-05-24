[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-2972f46106e565e64193e422d61a12cf1da4916b45550586e14ef0a7c637dd04.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=17303054)
# Problem Set 8

This problem set consists of 3 problems:
1. [Word analyzer](assignments/word_analyzer/README.md)
2. [Contacts app](assignments/contacts/README.md)
3. [Lottery analyzer](assignments/lotto/README.md)

# Help

<details>
  <summary><b>How to complete assignments</b></summary>

# Finding assignments

Assignments are contained in the [assignments](assignments) directory. There is one directory per assignment. Each assignment has specific instructions in the `README.md` file in the assignment directory.

For most assignments, you will be editing the file named `main.py` in the assignment directory. The instructions will explicitly note if other files need to be edited.

# Submitting

To submit assignments:
1. Find the relevant assignment in [our Gradescope class](https://www.gradescope.com/courses/840857)
1. Choose the option to submit via GitHub
   * Find your problem set repository in the list provided
   * You will need to allow Gradescope to access your GitHub account first - it will prompt you
1. The autograder will run your tests after you submit. You can view the results in Gradescope.
   * If your tests pass when you run them yourself, but fail in Gradescope, see the "Troubleshooting" below.
1. You can resubmit as many times as you want, up to the deadline.

## Troubleshooting submission

If your tests pass when you run them, but Gradescope tests fail:
1. Open the "terminal" in VSCode (the area where your programs print to when they run)
1. Run the following commands:
```
git pull --rebase
git push origin main
```
1. Resubmit to Gradescope

If you get any errors from the terminal commands, or Gradescope tests still fail after doing this,
reach out to the course staff for help.

For other issues with the Gradescope submission process, see
[Gradescope's article on submitting coding assignments](https://guides.gradescope.com/hc/en-us/articles/21865616724749-Submitting-a-Code-assignment)

# Editing and running code

Click on `main.py` in an assignment directory to open it. You can test your code manually by clicking the `Run` button at the top left of the text editor.

<img src=".images/code_play.png" width="400" />

</details>

<details>
  <summary><b>Testing your code</b></summary>

# Testing

You can always test your code manually by clicking on the `Run` button at the top right of the editor when you have a Python file open. This will run your program, and show its output in the terminal at the bottom.

Most assignments also come with automated tests. To run them, click on the `Testing` icon on the left side of VSCode, then click the "play" button on the test or tests you want to run.

<img src=".images/running_tests.png" width="300" />

**If you submit with any automated tests failing, you will not receive full credit for the assignment.**  Part of the challenge of the assignments is to make your code generate the output the tests are expecting. If your tests are failing - even if the failure seems trivial to you - you should try to fix them before submiting. Get help from the course staff if you feel stuck!

## Input / output tests

The early assignments in this class use input/output tests. These send input to your program, and ensure that your program produces the expected output. The actual output must match the expected output (almost) exactly - only blank lines are ignored.

### Understanding input/output failures

When you run input/output tests, if they fail, a side-by-side difference of the expected and actual output are automatically shown. If you have many failures, you may want to run a single test at a time.


<img src=".images/iotest_diff.png" width="800">

If you explore the "testcases" directories under each assignment, you can see each test case. They include:
1. `input.txt`: The input sent to your program
1. `expected.txt`: The expected output
1. (after you run at least once) `actual.txt`: The actual output your program produced the last time it ran

<img src=".images/iotest_find_files.png" width="800">

</details>

<details>
  <summary><b>Debugging your code</b></summary>

## Error messages

**Actually READ your error messages!**

While certain types of mistakes will produce messages that seem completely unrelated to the actual error,
most of the time the error message tells you what is wrong, and points out the offending line.

## Debugging via prints

Adding print statements to your code is an effective (if inelegant) way to understand why your code isn't behaving the way you expect it to.

Try:

* Printing hardcoded messages at certain points in the program, to see when (or if) your program reaches those points.
* Printing out the value of variables just before a conditional, to see why the conditional isn't working the way you expect
* Printing out the value of variables just before a crash, to see why your program is dying

## Debugger

Debuggers are tools that allow you to advance through a program, step by step, and examine the state of the
program at each step. They are very powerful tools.

VSCode has a Python debugger built in!

The typical flow is:
1. Set a "breakpoint" - a breakpoint is a place in the program where the debugger will pause when it is reached.
1. Launch the debugger
1. Once code execution reaches the breakpoint, examine the state of the program,
or continue stepping through line by line.

<img src=".images/debugger_launch.png" width="800" />

<img src=".images/debugger_tour.png" width="800">

</details>
