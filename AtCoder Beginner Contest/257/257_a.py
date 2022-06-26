string="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
A,B=list(map(int,input().split()))
moji=[]
for i in range(len(string)):
    for j in range(A):
        moji.append(string[i])

#print(moji)
print(moji[B-1])
