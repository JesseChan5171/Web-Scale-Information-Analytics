#!/usr/bin/env python
import sys
import operator

k = 100
store = dict()

for line in sys.stdin:
    word, count = line.strip().split('\t')
    if store.get(str(word)):
        store[str(word)] += int(count)
    else:
        store[str(word)] = int(count)

store_x = sorted(store.items(), key=operator.itemgetter(1))

# if len(store) > k - 1:
store_v = store_x[k-2][1]
for ele in store.keys():
    store[ele] -= int(store_v)
    if store[ele] <= 0:
        del store[ele]

for ele, count in store.items():
    print('%s\t%s' % (ele, count))

