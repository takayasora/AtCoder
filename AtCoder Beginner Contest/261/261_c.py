N=int(input())
mydict={}

for i in range(N):
    s=input()
    try:
        mydict[s]+=1
        print(s+"("+str(mydict[s])+")")
    except KeyError as e:
        mydict[s]=0
        print(s)