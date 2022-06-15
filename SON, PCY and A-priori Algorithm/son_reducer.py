#!/usr/bin/env python
import sys

prev_pair = None
for line in sys.stdin:
    pair, count = line.strip().split('\t')
    if pair == prev_pair:
        continue
    else:
        if prev_pair is not None:
            print(prev_pair)
        prev_pair = pair
if prev_pair == pair:
    print(pair)
