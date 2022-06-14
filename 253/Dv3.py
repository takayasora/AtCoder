import numpy as np

N,A,B=list(map(int,input().split()))

sum_num=np.arange(1,N,dtype=object).sum()
sum_numA=np.arange(0,N,A,dtype=object).sum()
sum_numB=np.arange(0,N,B,dtype=object).sum()

print(sum_num-sum_numA-sum_numB)

"""

sum_list=[]
for i in range(1,N+1):
    if(i%A!=0):
        None
    else:
        continue
    
    if(i%B!=0):
        None
    else:
        continue
    sum_list.append(i)
    
print(sum(sum_list))
"""
