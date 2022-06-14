#import sys
#import math
#from collections import deque
#import numpy as np
#import bisect
#import heapq

#N = list(map(int,input().stlip()))
N,K = list(map(int,input().split()))
#X,Y,Z = list(map(int,input().stlip()))
Slist=[]
Slist.append(input())
#print(Slist)

for i in range(K):
    moji=Slist[-1]
    Slist.append(moji[1:]+moji[0])
    
print(Slist)
unique_set = set(Slist)
unique_list = list(unique_set)
print(unique_list)

print(len(unique_list))
"""
if():

elif():

else:

"""
