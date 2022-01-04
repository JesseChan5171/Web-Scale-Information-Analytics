#!/usr/bin/env python
# Mapper
import sys
import itertools
from array import array
from decimal import *
from math import log

Cluster = 10
Dimension = 15 * 15

def main():
    pi = [0] * Cluster
    q = [ [] for i in range(Cluster)]
    with open("bin_2d.txt", "r") as fh:
        for line in fh:
            line = line.strip()
            cluster, cluster_pi, cluster_q_str = line.split("\t")
            cluster = int(cluster)
            pi[cluster] = float(cluster_pi)
            cluster_q = cluster_q_str.split(",")
            q[cluster] = map(float, cluster_q)

    N = 0
    Z = [0.0] * Cluster
    Zx = [ [0.0] * Dimension for i in range(Cluster)]
    log_prob = 0.0
    for line in sys.stdin:
        line = line.strip()
        vector = line.split(",")
        vector = filter(None, vector)
        x = map(int, vector)
        N += 1 #sum up the number of data point
        tem_k = [0.0] * Cluster 
        for i in range(Cluster):
            #scale up the probability so that it wouldn't equal to zero, does not affect the Znk value
            pk = map(lambda xi,qi: qi if xi == 1 else (1-qi), x, q[i]) 
            prob_k = reduce(lambda x, y: x * y, pk)
            tem_k[i] = prob_k * pi[i]
        for k in range(Cluster):
            Znk = tem_k[k] / sum(tem_k)
            log_prob += log(sum(tem_k)) #logarithm summation for the old model, regularize the probability
            Z[k] += Znk # sum up the assignment score z_nk for the k cluster
            temp_Zx = map(lambda xi: xi*Znk, x )
            Zx[k] = map(lambda x,y: x+y, Zx[k], temp_Zx) # sum up the z_nk*x_n for the k cluster
        
    for i in range(Cluster):
        Zx_str = map(str, Zx[i])
        print "%d\t%d\t%f\t%f\t%s" %(i, N, Z[i], log_prob, ",".join(Zx_str))
    
if __name__ == "__main__":
    main()
