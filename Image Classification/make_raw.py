import sys
from collections import defaultdict

fw = open("gplus_raw.txt","w")
data = defaultdict(set)
for line in open('gplus_combined.txt'):
    line = line.strip()
    follow, user = line.split(" ",1)
    data[user].add(follow)

for k,v in data.items():
    out = (k +" " +  " ".join(v)).replace(","," ")
    fw.write(out + "\n")
fw.close()
