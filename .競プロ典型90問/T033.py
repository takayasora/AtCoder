H,W=list(map(int,input().split()))

if H%2==0:
    light_H = H//2
else:
    light_H=H//2+1

if W%2==0:
    light_W = W//2
else:
    light_W=W//2+1

#print(light_H,light_W)
if(H==1):
    print(W)
elif(W==1):
    print(H)
else:
    print(light_H*light_W)


"""出力例）
2 3

# / #
/ / /

2
=============================================-

3 4
4

# / / #
/ / / /
# / / #


"""



"""
for i in range(H):
    for j in range(W):
        print(i*j , end="")
    print()

"""
