#!/usr/bin/env python
import sys

k = 100
store = dict()


for line in sys.stdin:
    words = line.strip().split()
    for word in words:
        if (not store.get(str(word))) and len(store) < k-1:
            store[str(word)] = 1
        elif store.get(str(word)):
            store[str(word)] += 1
        elif not store.get(str(word)):
            for ele in list(store.keys()):
                store[ele] -= 1
                if store[ele] <= 0:
                    del store[ele]

# store = dict(sorted(store.items(), key=lambda item: item[1]))

for ele, count in store.items():
    print('%s\t%s' % (ele, count))



