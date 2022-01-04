#!/usr/bin/env python
"""sm_mapper.py"""
import sys
from collections import defaultdict

# input comes from STDIN (standard input)
a = defaultdict(set)
for line in sys.stdin:
    nums = line.strip().split() 
    #print(nums[1],nums[0])
    a[str(line.replace('\n', '').split(' ')[1])].add(line.replace('\n', '').split(' ')[0])

for foll, followers in a.items():
    str_a = (foll+" "+ " ".join(followers)).replace(',','')
    print(str_a)
    #print(*followers,sep=" ")
