#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re

"""Baby Names exercise

Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 -Extract the year and print it
 -Extract the names and rank numbers and just print them
 -Get the names data into a dict and print it
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_names list
"""

def extract_names(filename):
  """
  Given a file name for baby.html, returns a list starting with the year string
  followed by the name-rank strings in alphabetical order.
  ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
  """
  f=open(filename, 'rU')
  file_text = f.read()
  res = []
  dict_names = {}

  # Parse the year
  year_line = re.findall(r'<h3 align="center">Popularity in (\d\d\d\d)</h3>', file_text)
  year_str = year_line[0]
  res.append(year_str)

  # Parse the names
  name_lines = re.findall(r'<tr align="right"><td>(\d+)</td><td>(\w+)</td><td>(\w+)</td>', file_text)
  for name_line in name_lines:
    boy_name = name_line[1]
    girl_name = name_line[2]
    rating = int(name_line[0])

    if boy_name in dict_names:
      if rating < dict_names[boy_name]:
        dict_names[boy_name] = rating  
    else:
      dict_names[boy_name] = rating

    if girl_name in dict_names:
      if rating < dict_names[girl_name]:
        dict_names[girl_name] += rating
    else:
      dict_names[girl_name] = rating

  for i in dict_names.items():
    res.append(i[0] + ' ' +str(i[1]))
    #print i[0] + '->' + str(i[1])

    #print name_line[1] + '->' + name_line[0] + ', ' + name_line[2] + '->' + name_line[0]
  
  res = sorted(res[:])
  '''
  for i in res:
    print i
  '''
  f.close()
  return res


def main():
  # This command-line parsing code is provided.
  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]

  if not args:
    print 'usage: [--summaryfile] file [file ...]'
    sys.exit(1)

  # Notice the summary flag and remove it from args if it is present.
  summary = False
  if args[0] == '--summaryfile':
    summary = True
    del args[0]

    for filename in args:
      names_list = extract_names(filename)
      f = open(filename+'.summary', 'w')
      for name_line in names_list:
        f.write(name_line + '\n')
      f.close()

  else:
    names_list = extract_names(args[0])
    for name_line in names_list:
      print(name_line)


  
  # For each filename, get the names, then either print the text output
  # or write it to a summary file
  
if __name__ == '__main__':
  main()
