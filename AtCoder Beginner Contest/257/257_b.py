N,K,Q = list(map(int, input().split()))
Alist = list(map(int, input().split()))
Llist = list(map(int, input().split()))
#print(Alist)
for i in range(len(Llist)):
    #print(i,"========")
    #print(Alist[Llist[i]-1])
    #print(N)
    #print(type(Alist[Llist[i]-1]))
    #print(type(N))
    if Alist[Llist[i]-1]==N:
        #print("bigcon")
        continue
    if Alist[Llist[i]-1]+1 in Alist:
        #print("onazicon")
        continue
    Alist[Llist[i]-1]+=1
    #print(Alist)

Alist = [str(i) for i in Alist]
str = ' '.join(Alist)
print(str)
