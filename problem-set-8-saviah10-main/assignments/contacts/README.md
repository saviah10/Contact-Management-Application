# Contacts App

Skills for this problem: `Data types`, `String escaping`, `Lists - initialization, modification`,
`Lists - iteration`, `Lists - nested lists`, `References`, `Dictionaries - initialization, modification`,
`Dictionaries - iteration`, `Sorting`, `Nested data structures`, `Sets`,
`Data structures - choosing appropriately`

In this problem, you will write a contacts application that keeps track of phone numbers for your
contacts.

## Requirements

Write a program that repeatedly prompts the user to take one of the following actions, until they
select #5 (Quit):
1. Add a phone number to a contact
   * When selecting this, the user should be prompted for the contact name and the phone number
     (in that order)
   * **Phone numbers for a contact are unique**. A single contact can't have the same phone number
     more than once. It's ok for multiple different contacts to have the same number.
      * e.g. It is not allowed for `Joe` to have the phone numbers: `[123, 123]`
      * e.g. It **is** allowed for `Joe` to have the numbers `[123, 456]` and `Bob` to also have the
        numbers `[123, 456]`.
2. Delete a contact
   * When selecting this, the user should be prompted for the contact name to delete.
   * Attempting to delete a non-existent contact should print an error message:
     `"Name not found. Try again."` and then prompt the user for a new action.
3. Print a contact
   * When selecting this, the user should be prompted for the contact name to print.
   * Attempting to print a non-existent contact should print an error message:
     `"Name not found. Try again."` and then prompt the user for a new action.
4. Print the name of the contact with the most phone numbers.
5. Quit

## Grading notes

1. In order to earn the `References` skill, you must not use **any** global variables.
1. In order to earn the `Functional Decomposition` skill, you must use a helper function for each
   action.
1. In order to earn the `Data structures - choosing appropriately` skill, you must choose the best
   data structures in which to store your contact data, given the problem requirements.
   * Hint: the different data types we've discussed are: `int`, `float`, `str`, `bool`,
      `list`, `dict` and `set`.

## Sample output

Sample output is found below. See [testcases](testcases) for more examples.

```
Welcome to the contacts app!
1. Add a phone number
2. Delete a contact
3. Print a contact
4. Print contact with most phone numbers
5. Quit
What would you like to do?
1
Contact name?
Joe
Phone number?
123
Added number: 123 for Joe
1. Add a phone number
2. Delete a contact
3. Print a contact
4. Print contact with most phone numbers
5. Quit
What would you like to do?
3
Contact name?
Joe
Contact "Joe":
Phone numbers:
123
1. Add a phone number
2. Delete a contact
3. Print a contact
4. Print contact with most phone numbers
5. Quit
What would you like to do?
1
Contact name?
Joe
Phone number?
345
Added number: 345 for Joe
1. Add a phone number
2. Delete a contact
3. Print a contact
4. Print contact with most phone numbers
5. Quit
What would you like to do?
3
Contact name?
Joe
Contact "Joe":
Phone numbers:
123
345
1. Add a phone number
2. Delete a contact
3. Print a contact
4. Print contact with most phone numbers
5. Quit
What would you like to do?
1
Contact name?
Joe
Phone number?
123
Added number: 123 for Joe
1. Add a phone number
2. Delete a contact
3. Print a contact
4. Print contact with most phone numbers
5. Quit
What would you like to do?
3
Contact name?
Joe
Contact "Joe":
Phone numbers:
123
345
1. Add a phone number
2. Delete a contact
3. Print a contact
4. Print contact with most phone numbers
5. Quit
What would you like to do?
5
Bye!
```