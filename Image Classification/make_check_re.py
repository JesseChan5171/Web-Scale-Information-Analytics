import sys
from collections import defaultdict

#fw = open("Thecombine.txt","r")
num = input("The First One ")
num2 = input("The Second One ")
for line in open('twitter_raw.txt'):
    line = line.strip()
    user, follower = line.split(" ",1)
    if int(user) == num:
        print('The first one is' +' '+  follower)
        set1 = set()
	for i in follower.split():
	    set1.add(i)
    if int(user) == num2:
        print('The second one is' + ' '+ follower)
        set2 = set()
	for i in follower.split():
            set2.add(i)

#print(set1)
#print(set2)
sim = float(len(set1.intersection(set2)))/len(set1.union(set2))
print('The similarity is', sim)


