# Contact-Management-Application

## What it is
A command-line contacts app built in Python that lets users add, delete, and look up contacts and their phone numbers.

## Why
Built to practice choosing the right data structure for a real constraint: each contact needed fast lookups by name, plus a way to guarantee no duplicate phone numbers per contact without extra logic. This became a functional decomposition exercise as much as a data structures one.

## Key features
- Add phone numbers to a contact, duplicates for that contact are automatically prevented
- Delete a contact by name
- Print a contact's full list of phone numbers, sorted
- Find and print the contact with the most phone numbers

## Challenges
The trickiest part was picking the right structure for phone numbers. A list would allow duplicate numbers per contact, which the requirements explicitly ruled out. Switching to a set for each contact's numbers meant duplicates were rejected automatically, no manual duplicate-checking logic needed. Dictionaries handled the name-to-numbers mapping so lookups stayed fast instead of scanning a list every time.

## Setup
\```
python main.py
\```

## Tech
Python, using dictionaries and sets for core data storage (no external libraries)
