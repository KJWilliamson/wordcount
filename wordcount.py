#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

"""Wordcount exercise

The main() function is already defined and complete. It calls the
print_words() and print_top() functions, which you fill in.

See the README for instructions.

Use str.split() (no arguments) to split on all whitespace.

Workflow: don't build the whole program at once. Get it to an intermediate
milestone and print your data structure. Once that's working, try for the
next milestone.

Implement the create_word_dict() helper function that has been defined in
order to avoid code duplication within print_words() and print_top(). It
should return a dictionary with words as keys, and their counts as values.
"""

# Your name, plus anyone who helped you with this assignment
# Give credit where credit is due.
__author__ = "Kamela Williamson"
# worked on it with Mai and Cesar helped us a lot!

import sys


def create_word_dict(filename):
    """Returns a word/count dict for the given file."""
    # filename = filename.strip()
    # Your code here
    create_word = {}
    with open(filename, 'r') as file:
        words = file.read().split()
        for word in words:
            word = word.lower()
            if word in create_word.keys():
                create_word[word] += 1
            else:
                create_word[word] = 1

    return(create_word)


def print_words(filename):
    """Prints one per line '<word> : <count>', sorted
    by word for the given file.
    """
    # Your code here
    word_count = sorted(create_word_dict(filename).items())
    for tup in word_count:
        print(tup)


def print_top(filename):
    """Prints the top count listing for the given file."""
    # Your code here
    word_count = list(create_word_dict(filename).items())
    words = sorted(word_count, key=lambda x: x[-1], reverse=True)
    for tup in words[:20]:
        print(tup)

    return


# This basic command line argument parsing code is provided and calls
# the print_words() and print_top() functions which you must implement.
def main(args):
    if len(args) != 2:
        print('usage: python wordcount.py {--count | --topcount} file')
        sys.exit(1)

    option = args[0]
    filename = args[1]

    if option == '--count':
        print_words(filename)
    elif option == '--topcount':
        print_top(filename)
    else:
        print('unknown option: ' + option)


if __name__ == '__main__':
    main(sys.argv[1:])
