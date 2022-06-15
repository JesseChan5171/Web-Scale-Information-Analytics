#!/usr/bin/env python
"""sm_mapper.py"""
import sys
from collections import defaultdict

# input comes from STDIN (standard input)
a = defaultdict(set)
for line in sys.stdin:
     for i in line.split()[1:]:
         a[str(line.split(' ')[0])].add(i) 
b = defaultdict(set)
infile = "facebook_raw.txt"
with open(infile, 'rt') as f_i:
    for line in f_i.readlines():
        for i in line.split()[1:]:
           b[str(line.split(' ')[0])].add(i) 
    len_b = len(b)
    #sim_mat = [[0 for x in range(len_b)] for y in range(len_b)]
    for v,k in a.items():
        for j,y in b.items():
            if len(k.union(y)) == 0:
               # sim_mat[int(v)][int(j)] = 0
	        print(v,j,0)
            else:
                #sim_mat[int(v)][int(j)] = len(k.intersection(y))/len(k.union(y));
		#print()
		print(v,j,float(len(k.intersection(y)))/len(k.union(y)))
