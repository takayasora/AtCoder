S=input()
flag=-1

while(1):
    if flag==0:
        break
    flag=0
    if(S.endswith('dream')):
        S=S[:-5]
        flag=1
    if(S.endswith('dreamer')):
        S=S[:-7]
        flag=1
    if(S.endswith('erase')):
        S=S[:-5]
        flag=1
    if(S.endswith('eraser')):
        S=S[:-6]
        flag=1
print("YES") if len(S)==0 else print("NO")
