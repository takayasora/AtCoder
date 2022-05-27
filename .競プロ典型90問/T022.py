a,b,c=list(map(int,input().split()))

x=a
y=b
z=c
temp=0
while(1):
    if(x>=y):
        x=x%y
        if(x==0):
            temp=y
            break
    else:
        y=y%x
        if(y==0):
            temp=x
            break

while(1):
    if(temp>=z):
        temp=temp%z
        if(temp==0):
            r=z
            break
    else:
        z=z%temp
        if(z==0):
            r=temp
            break

print((a//r-1)+(b//r-1)+(c//r-1))
