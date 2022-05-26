def main():
    H,W=list(map(int,input().split()))
    R,C=list(map(int,input().split()))
    print(question(H,W,R,C))

def question(H,W,R,C):
    ans=0
    ans+=1 if R>1 else None
    ans+=1 if R<H else None
    ans+=1 if C>1 else None
    ans+=1 if C<W else None
    
    return ans


main()
