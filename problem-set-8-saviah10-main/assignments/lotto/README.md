# Lottery analyzer

Skills for this problem: `Variables`, `Expressions`, `Conditionals - if/elif/else`,
`Conditionals - logic`, `Functions - invocation`, `Functions - definition`, `Functions - parameters`,
`Functions - returning`, `Cumulative algorithm`, `Loops - choosing appropriate structure`,
`Lists - initialization, modification`, `Lists - iteration`, `Lists - nested lists`,
`String manipulation`, `Tuples`, `Dictionaries - initialization, modification`,
`Nested data structures`, `File I/O`, `File I/O - CSVs`

Our next get rich quick scheme: analyze old winning lottery numbers to predict which numbers are
most likely to win.

You will write some tools that will read in a CSV file containing historical lottery data, and
analyze it.

## Requirements

The CSV file used in this problem is [numbers.csv](numbers.csv).

Implement the following functions:

* `load_file(filename)`: This function takes in a filename as an argument, and loads CSV data from it.
   * The CSV file is **tab-delimited**
   * The CSV file contains a header row
   * The fields in the CSV file are: date, winning numbers, and "multiplier"
   * Here is an example row: `9/28/19	15 23 34 51 55 04	2`
   * This function should return a list of lists: the outer list contains one entry for each row,
     and each inner lists contains a date, winning set of numbers, and a multiplier.
* `find_winner(date, data)`: This function takes in a date, and the loaded data, and returns
  the winning numbers for that date. If there was no winner on that date, the function returns `None`
   * `date` will be a string, in the same format that is stored in the file.
      * There is no need to do any date manipulation for this assignment, just compare the date strings.
   * `data` will be the return value of `load_file`
* `find_days_with_number(number, data)`: This function returns all dates on which `number` was one
  of the winning numbers.
   * Note that each day has 6 winning numbers. A day matches if any of those 6 numbers was `number`.
   * The return value should be a list, containing the matching dates as strings.
   * `data` will be the return value of `load_file`
* `count_winning_numbers(numbers, data)`: This function counts how many times each individual number was
  part of a winning set of numbers.
   * The function should return a dictionary, where the keys are the numbers, and the values are the
     number of times that number appeared as a winner.
   * The keys in the dictionary should be strings, formatted the same way they are found in the file:
     with a leading zero for single digit numbers - e.g. `"01"` or `"09"`
   * You may not need this, but you can use an f-string trick to pad a number with leading zeros:
     `f"{x:02}"` will convert `x` to a string, and pad it with leading `0`s if the string is shorter
     than 2 characters.
   * `data` will be the return value of `load_file`
* `find_best_number(data)`: Find the number that appeared as a winner the most times
   * The return value should be a 2-tuple: the most-winning number (`str`), and the number of times it
     appeared (`int`)
   * The most-winning number should be formatted as a string, with a leading zero for single digit
     numbers.
   * `data` will be the return value of `load_file`
   * Hint: one of the other functions that you already wrote for this problem will be very useful
     when implementing this function...

Unit tests are provided. You are welcome to add more tests, but it is not required for this problem.