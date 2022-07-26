import itertools

N,M = list(map(int, input().split()))
xlist = list(map(int, input().split()))

mydict={}
for i in range(M):
    C,Y=list(map(int,input().split()))
    mydict[C]=Y

maxlist=[0.0,0,0]
for key,item in mydict.items():
    if N<key:
        continue
    if maxlist[0]<(item/key):
        maxlist[0]=item/key
        maxlist[1]=key
        maxlist[2]=item

print("=========================")
counter=1
sum_ans=xlist[0]
try:
    sum_ans+=mydict[counter]
except KeyError:
    None
for i in range(1,N-maxlist[1]):
    print(i,sum_ans)
    if i%maxlist[1]!=0:
        sum_ans+=xlist[i]
        counter+=1
        try:
            sum_ans+=mydict[counter]
        except KeyError:
            None
    else:
        counter=0
    print(counter)

for j in range(N-maxlist[1],N):
    print(j,sum_ans)
    sum_ans+=xlist[j]
    counter+=1
    try:
        sum_ans+=mydict[counter]
    except KeyError:
        None
    print(counter)
    

print(sum_ans)

