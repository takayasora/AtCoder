H,W = list(map(int, input().split()))

a = []

for i in range(int(H)):
    A = input()
    B = list(A)
    a.append(B)

#print(a)

point=[]
for i in range(H):
    for j in range(W):
        #print(a[i][j])
        if (a[i][j]=="o"):
            point.append(i)
            point.append(j)

print(abs(point[0]-point[2])+abs(point[1]-point[3]))
