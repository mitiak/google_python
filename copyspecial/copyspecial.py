#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os
import shutil
import commands

"""Copy Special exercise
"""

def ListSpecial(dir):
  filenames = os.listdir(dir)
  special_files = []
  for filename in filenames:
    match = re.search(r'__\w+__',filename)
    if match:
      abspath = os.path.abspath(os.path.join(dir, filename))
      print abspath
      special_files.append(abspath)
  return special_files


def CopyToDir(files, todir):
  # Create the directory if needed
  cmd = 'ls -l ' + todir
  (cmd_status, _) = commands.getstatusoutput(cmd)
  if cmd_status:
    os.mkdir(todir)
    print todir + ' created.'
  else:
    print todir + ' found.'

  # Copy the files
  for file in files:
    print 'shutil.copy('+file+', '+todir+')'
    shutil.copy(file, todir)
  return
  
  

def main():
  # This basic command line argument parsing code is provided.
  # Add code to call your functions below.

  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]
  if not args:
    print "usage: [--todir dir][--tozip zipfile] dir [dir ...]";
    sys.exit(1)

  # todir and tozip are either set from command line
  # or left as the empty string.
  # The args array is left just containing the dirs.
  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]

  tozip = ''
  if args[0] == '--tozip':
    tozip = args[1]
    del args[0:2]

  if len(args) == 0:
    print "error: must specify one or more dirs"
    sys.exit(1)

  special_files = ListSpecial(args[0])

  if todir:
    CopyToDir(special_files, todir)
  
if __name__ == "__main__":
  main()
