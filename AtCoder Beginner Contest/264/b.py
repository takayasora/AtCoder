R,C=list(map(int,input().split()))
if R==C:
    print("white") if C%2 else print("black")
elif R+C==16:
    print("white") if C%2 else print("black")
else:
    print("white") if abs(R-C)%2 else print("black")