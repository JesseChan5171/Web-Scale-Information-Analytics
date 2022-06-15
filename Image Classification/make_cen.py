import random as rnd
import math
import numpy as np

def rand_cen():
    file_name = "cen_1.txt"
    with open(file_name, "a") as f:
        for i in range(0, 37):
	    f.write(str(i)+'\t')
            for j in range(0, 784):
                f.write(str(rnd.randint(0, 255)))
                f.write(' ')
            f.write('\n')

rand_cen()
