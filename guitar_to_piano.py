#!/usr/bin/python
# -*- coding: utf-8 -*-


import sys

BASE = [4, 9, 14, 19, 23, 28];

NOTE = ['1', '1#', '2', '2#', '3', '4', '4#', '5', '5#', '6', '6#', '7'];

def main():
  bar = 1
  base = 5
  with open(sys.argv[1], 'r') as f:
    for line in f:
      line = line.strip()
      if not line:
        base = 5
        print
        continue
      notes = line.split()
      out_notes = []
      for note in notes:
        if note == '-':
          out_notes.append('-')
          continue

        n = int(note) + BASE[base]
        out = ''
        if n >= 12:
          out += '('
        out += NOTE[n % 12]
        out += '.' * (n/12) 
        if n >= 12:
          out += ')'
        out_notes.append(out)
      if base == 5:
        print 'bar %s' % bar
        bar += 1
      print ' '.join(['%-10s' % n for n in out_notes])
      base = base - 1 if base > 0 else 5

main()
