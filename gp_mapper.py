#!/usr/bin/env python
"""sm_mapper.py"""
import sys
from collections import defaultdict

# input comes from STDIN (standard input)
a = defaultdict(set)
for line in sys.stdin:
    nums = line.strip().split() 
    #print(nums[1],nums[0])
    print("%s\t%s"%(nums[1],nums[0]))

