#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

"""Wordcount exercise
Google's Python class

The main() below is already defined and complete. It calls print_words()
and print_top() functions which you write.

1. For the --count flag, implement a print_words(filename) function that counts
how often each word appears in the text and prints:
word1 count1
word2 count2
...

Print the above list in order sorted by word (python will sort punctuation to
come before letters -- that's fine). Store all the words as lowercase,
so 'The' and 'the' count as the same word.

2. For the --topcount flag, implement a print_top(filename) which is similar
to print_words() but which prints just the top 20 most common words sorted
so the most common word is first, then the next most common, and so on.

Use str.split() (no arguments) to split on all whitespace.

Workflow: don't build the whole program at once. Get it to an intermediate
milestone and print your data structure and sys.exit(0).
When that's working, try for the next milestone.

Optional: define a helper function to avoid code duplication inside
print_words() and print_top().

"""

import sys

# Prints the given dictionary by key in sorted order
def print_dict_by_word(dict):
  for k in sorted(dict.keys()):
    print k + ' -> ' + str(dict[k])


# Helper function to sort by word count
def sort_by_cnt(item):
  return item[1]

# Prints num_to_print items from the given dictionary ordered by words count
def print_dict_by_cnt(file_dict, num_to_print):
  cnt_printed = 0
  for i in sorted(file_dict.items(), key=sort_by_cnt, reverse=True):
    print i[0] + ' -> ' + str(i[1])
    cnt_printed += 1
    if cnt_printed == num_to_print:
      break

# Builds the dictionary from the given file
def build_dict(filename):
  res_dict = {}
  file = open(filename, 'rU')

  if file == None:
     return

  txt_filetext = file.read()
  lst_words = txt_filetext.split()

  for word in lst_words:
    word = word.lower()
    if word in res_dict.keys():
      res_dict[word] += 1
    else:
      res_dict[word] = 1

  file.close()
  return res_dict

# Define print_words(filename) and print_top(filename) functions.
# You could write a helper utility function that reads a file
# and builds and returns a word/count dict for it.
# Then print_words() and print_top() can just call the utility function.

def print_top(filename):
  file_dict = build_dict(filename)
  print_dict_by_cnt(file_dict, 5)
  return

def print_words(filename):
  file_dict = build_dict(filename)
  print_dict_by_word(file_dict)
  return


# This basic command line argument parsing code is provided and
# calls the print_words() and print_top() functions which you must define.
def main():
  if len(sys.argv) != 3:
    print 'usage: ./wordcount.py {--count | --topcount} file'
    sys.exit(1)

  option = sys.argv[1]
  filename = sys.argv[2]
  if option == '--count':
    print_words(filename)
  elif option == '--topcount':
    print_top(filename)
  else:
    print 'unknown option: ' + option
    sys.exit(1)

if __name__ == '__main__':
  main()
