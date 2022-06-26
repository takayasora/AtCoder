import numpy as np

N,A,B=list(map(int,input().split()))


np.arange(1,N).sum()



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
