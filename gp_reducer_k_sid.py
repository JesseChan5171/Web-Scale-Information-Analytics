#!/usr/bin/env python
"""md_mapper.py"""
import sys
from collections import defaultdict
from collections import Counter

# input comes from STDIN (standard input)
b = defaultdict(set)
infile = "gplus_raw.txt"
set_a = {0, 0, 9, 8, 3}
set_b = set()
with open(infile, 'rt') as f_i:
    for line in f_i.readlines():
        for i in line.strip().split()[1:]:
            b[str(line.strip().split(' ')[0])].add(i)
a = defaultdict(set)
#set_b = {"0":0,"1":0,"2":0}
set_b_k = []
for line in sys.stdin:
   # for i in line.split()[1:]:
    a[str(line.strip().split('\t')[0])].add(line.strip().split('\t')[1])

for v,k in a.items():
    
    if not(str(v).endswith('00001')):
        continue 
    max_v = 0
    max_k = 0
    set_b = {"0":0,"1":0,"2":0}
    for j,y in b.items():
        if len(k.union(y)) == 0 or v == j:
            pass
        else:
            new_v = float(len(k.intersection(y)))/len(k.union(y))
            if new_v > min(set_b.values()):
  	        set_b[str(j)] = new_v
   	        #c = Counter(set_b)
		#set_b = c.most_common(3)
		#set_b = sorted([(x, i) for (i, x) in enumerate(set_b)], reverse=True)[:3]
		#if new_v in set_b:
		    #set_b_k.append(v)
    c = Counter(set_b)
    mc = c.most_common(3)
    
    for key,val in mc:
        set_c = b[str(key)].intersection(k)
        set_sum = sum(map(int,list(set_c)))
#       print("%s:%s\t%s\t check_sum=%d" % (v,key ,list(set_c), set_sum))
        print("{}:{}\t{} check_sun = {}".format(v,key,list(set_c),set_sum)) 
