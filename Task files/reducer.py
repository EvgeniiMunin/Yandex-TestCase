#! /usr/bin/env python
"""reducer.py"""

from __future__ import print_function
import sys
from math import sqrt
from scipy.stats import t


curr_type_query = None
curr_count_value = 0
curr_mean_value = 0
curr_std_value = 0
type_query = None

# 95% confidence interval
confidence = 0.95

# input comes from STDIN
for line in sys.stdin:
    # split the line
    # key: type_query
    # values: time_query, count_query, std_query, time_min, time_max
    type_query, mean_query, count_query, std_query, _, _ = line.split('\t')

    # convert types from str
    mean_query = float(mean_query)
    count_query = int(count_query)
    std_query = float(std_query)
    
    if curr_type_query == type_query:
        # save old mean value for var calculation
        old_mean_value = curr_mean_value
        # mean value calculation
        curr_mean_value = (curr_count_value*curr_mean_value + count_query*mean_query) / (curr_count_value + count_query)
        # std value calculation
        # https://en.wikipedia.org/wiki/Algorithms_for_calculating_variance#Parallel_algorithm
        delta = old_mean_value - mean_query
        m_a = curr_std_value*(curr_count_value - 1)
        m_b = std_query*(count_query - 1)
        M2 = m_a + m_b + delta**2 * curr_count_value * count_query / (curr_count_value + count_query)
        curr_std_value = sqrt(M2 / (curr_count_value + count_query - 1))
        # counter increase
        curr_count_value += count_query
    else:
        # output statistics when new type_query encountered
        if curr_type_query:
            t_stat = t.ppf((1+confidence)/2., curr_count_value-1)
            delta = t_stat * curr_std_value / sqrt(curr_count_value)
            time_min = curr_mean_value - delta
            time_max = curr_mean_value + delta
            # key: type_query
            # values: time_query, count_query, std_query, time_min, time_max
            print('{}\t{}\t{}\t{}\t{}\t{}'.format(curr_type_query, curr_mean_value, curr_count_value, curr_std_value, time_min, time_max))
        curr_type_query = type_query
        curr_count_value = count_query
        curr_mean_value = mean_query
        curr_std_value = std_query
    
# output the last query
# key: type_query
# values: time_query, count_query, std_query, time_min, time_max
if curr_type_query == type_query:
    print('{}\t{}\t{}\t{}\t{}\t{}'.format(curr_type_query, curr_mean_value, curr_count_value, curr_std_value, time_min, time_max))
