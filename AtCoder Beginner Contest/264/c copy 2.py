#入力値の読み込み
Ha,Wa=list(map(int,input().split()))
Alist=[]
for i in range(Ha):
    templist=[]
    templist=input()
    Alist.append(templist)

Hb,Wb=list(map(int,input().split()))
Blist=[]
for i in range(Hb):
    templist=[]
    templist=input()
    Blist.append(templist)

#print(Alist)
#print(Blist)


import re
mathclist=[]
for i in range(len(Blist)):
    pattern=Blist[i].replace(" ",r"*")
    print(pattern)
    pattern=r"*"+pattern+r"*"
    print(pattern)
    for j in range(len(Alist)):
        if re.match(pattern,Alist[j]):
            mathclist.append(j)

new_list = sorted(mathclist)
#print(new_list)
#print(mathclist)
if len(mathclist)==Hb: 
    if new_list==mathclist:
        print("Yes")
    else:
        print("No")
else:
    print("No")