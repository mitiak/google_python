#!/usr/bin/python

import sys
import os
import commands

def List(dir):
  cmd = 'ls -l ' + dir
  #print 'about to do: \"' + cmd + "\""
  #return
  (status, output) = commands.getstatusoutput(cmd)
  if status:
    sys.stderr.write('error: ' + output + '\n')
    sys.exit(1)
  print status
  print output
  '''
  filenames = os.listdir(dir)
  for filename in filenames:
    path = os.path.join(dir, filename)
    print path
    print os.path.abspath(path)
'''
def main():
  List(sys.argv[1])

if __name__ == '__main__':
  main()