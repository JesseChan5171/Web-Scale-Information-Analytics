import random as rnd
import math
import numpy as np

a = dict()
#centroid_list = []
blf = open("bin_t_2.txt").readlines()

def rand_cen():
    count = 0
    file_name = "cen_1.txt"
    for i in open("label_out.txt",'r').readlines():
        i = int(i.strip())-1
        if not a.get(str(i)):
            a[str(i)] = count
        elif not a.get(str(i+26)):
            a[str(i+11)] = count
        count+=1

    with open(file_name,"w") as bf:
        for k,v in a.items():
            str_l = str(str(k) + '\t' + str((blf[int(v)])))
            bf.write(str_l)
            #bf.write('\n')

rand_cen()
