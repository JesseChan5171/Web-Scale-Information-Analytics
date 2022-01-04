#!/usr/bin/env python
"""md_mapper.py"""
import sys
from collections import defaultdict

# input comes from STDIN (standard input)
b = defaultdict(set)
infile = "twitter_raw.txt"
#set_a = {2, 4, 9, 8, 3}
#set_b = set()
with open(infile, 'rt') as f_i:
    for line in f_i.readlines():
        for i in line.strip().split()[1:]:
            b[str(line.strip().split(' ')[0])].add(i)
a = defaultdict(set)
for line in sys.stdin:
   # for i in line.split()[1:]:
    a[str(line.strip().split('\t')[0])].add(line.strip().split('\t')[1])

for v,k in a.items():
    #set_b = set()
    #for j in list(str(v)):
	#set_b.add(int(j))
    #print(set_b)
    if not(str(v).endswith('24983')):
        continue
    max_v = 0
    max_k = 0
    for j,y in b.items():
        if len(k.union(y)) == 0 or v == j:
            pass
        else:
            new_v = float(len(k.intersection(y)))/len(k.union(y))
            if new_v > max_v:
                max_v = new_v
                max_k = j
    print("%s\t%s\t%s" % (v, max_k, max_v))
    #print(set_a , set_b)
