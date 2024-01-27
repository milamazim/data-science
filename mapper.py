#!/usr/bin/env python3

import sys

try:
  for line in sys.stdin:
    words = line.split()
    for word in words:
      print('{0}\t{1}'.format(word, 1))
except Exception as e:
  raise(e)