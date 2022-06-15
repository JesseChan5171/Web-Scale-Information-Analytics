#!/usr/bin/env python

import sys
import numpy as np
k = 37
wh_v = np.zeros((k, 784), dtype='float')
wh_sum = np.zeros(k)

arr_count_cen_v = np.zeros(k)
arr_count_cen = np.zeros(k)

# #for line in sys.stdin:
for line in sys.stdin:
    num_clu = int(line.strip().split('\t')[0])
    part_sum = float(line.strip().split('\t')[1])
    part_v = line.strip().split('\t')[2]

    arr_part_v = []
    for i in part_v.strip().split():
        arr_part_v.append(float(i))
    arr_part_v = np.asarray(arr_part_v)

    for i in range(0, 784):
        c = wh_v[num_clu][i] + arr_part_v[i]
        wh_v[num_clu][i] = c

    arr_count_cen[num_clu] += 1
    wh_sum[num_clu] = wh_sum[num_clu] + part_sum
    arr_count_cen_v[num_clu] += 1

for i in range(0, k):
    if arr_count_cen[i] > 0:
        print('%s\t%s' % (i, ' '.join(map(str, (wh_v[i] / arr_count_cen[i])))))
