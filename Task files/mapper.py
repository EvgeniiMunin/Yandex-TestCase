#!/usr/bin/env python
"""mapper.py"""

from __future__ import print_function
import sys
import numpy

# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # split the line
    num_query, type_query, time_query = line.split(',')
    # increase counters
    # key: type_query
    # values: time_query, count_query, var_query, time_min, time_max
    print('{}\t{}\t{}\t{}\t{}\t{}'.format(type_query, time_query, 1, 0, 0, 0))
