#!/usr/bin/env python
import sys
import math
import numpy as np
k = 37

cen = np.zeros((k, 784))
up_cen = np.zeros((k, 784))
arr_cen = np.zeros(k)

arr_count_cen_v = np.ones(k)
arr_count_cen = np.ones(k)


def p_c_distance(pt, index_cen):
    dist = 0
    result = pt - cen[index_cen]
    dist += np.sum((result*result))
    return dist

def read_to_cen():
    with open("cen_1.txt", "r") as f_c:
        # count = 0
        for i in f_c.readlines():
            x = []
            j = i.strip().split('\t')[0]
            k = i.strip().split('\t')[1]
            for item in k.strip().split():
                x.append(float(item))
            x = np.array(x)
            cen[int(j)] = x
            # count += 1

def tran_a(pt):
    x = []
    for i in pt.strip().split():
        x.append(float(i))
    x = np.asarray(x)
    return x

def cal_new_cen(pt, pos):
    new_v = pt
    new_v = np.array(new_v)
    # for j in range(0, 784):
    up_cen[pos] = up_cen[pos] + new_v
    arr_count_cen[pos] += 1

read_to_cen()
up_cen = cen.copy()

# sys.stdin

for line in sys.stdin:
    min_d = 99999999999
    pos = 53
    line = tran_a(line)
    for i in range(0, k):
        dist = p_c_distance(line, i)
        if min_d > dist:
            min_d = dist
            pos = i
    arr_cen[pos] = arr_cen[pos] + min_d
    arr_count_cen_v[pos] += 1
    cal_new_cen(line, pos)


for i in range(0, k):
    print(
        '%s\t%s\t%s' % (i, arr_cen[i] / int(arr_count_cen_v[i]), ' '.join(map(str, (up_cen[i] / int(arr_count_cen[i]))))))

