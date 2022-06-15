#!/usr/bin/env python
# Reducer
import sys
import itertools
from array import array
from decimal import *

Cluster = 10
Dimension = 28 * 28

def main():

    N = [0] * Cluster
    pi = [0] * Cluster
    q = [ [] for i in range(Cluster)]
    
    cluster_now = -1
    N_now = 0
    Z_now = 0.0
    Zx_now = [0.0] * Dimension
    total_prob = 0.0
    for line in sys.stdin:
        line = line.strip()
        cluster, data_num, zk_sum, log_prob, zkx_sum = line.split("\t")
        zkx_sum = zkx_sum.split(",")
        cluster = int(cluster)
        if cluster != cluster_now:
            if cluster_now != -1:
                N[cluster_now] = N_now
                pi[cluster_now] = Z_now/N_now
                q[cluster_now] = map(lambda x: x/Z_now, Zx_now)
            N_now = 0
            Z_now = 0.0
            Zx_now = [0.0] * Dimension
            total_prob = 0.0
            cluster_now = cluster
        N_now += int(data_num)
        Z_now += float(zk_sum)
        zkx_sum = map(float, zkx_sum)
        total_prob += float(log_prob)
        Zx_now = map(lambda x,y: x+y, Zx_now, zkx_sum)

    # output the last cluster 
    N[cluster_now] = N_now
    pi[cluster_now] = Z_now/N_now
    q[cluster_now] = map(lambda x: x/Z_now, Zx_now)

    # normalize the pi parameter so that it equals to 1 
    pi = map(lambda x: Decimal(0.0001) if x == 0 else Decimal(x), pi)

    for i in range(Cluster):
        pi[i] = pi[i] / sum(pi)
    print "%f" %(total_prob)
    for i in range(Cluster):
        if N[i] != 0:
            print "%d\t%s\t%s" %(i, str(pi[i]), ",".join(map(str, q[i])) )

if __name__ == "__main__":
    main()
