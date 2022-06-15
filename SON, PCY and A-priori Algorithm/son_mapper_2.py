#!/usr/bin/env python

import sys

file = 'freq_pair.txt'

threshold = 0.005

freq_pair = {}

with open(file) as f:
    lines = f.readlines()
    for line in lines:
        pair = line.strip()
        freq_pair[pair] = 0

for line in sys.stdin:
    line = line.strip()
    words = line.split()
    words = list(set(words))
    for j in range (0,len(words)-1):
        for k in range(j+1,len(words)):
            if(words[j]<=words[k]):
                pair = words[j]+","+words[k]
            else:
                pair = words[k]+","+words[j]
            if pair in freq_pair:
                freq_pair[pair] += 1
	    else:
		continue
for pair in freq_pair:
    print('%s\t%s' % (pair, freq_pair[pair]))
