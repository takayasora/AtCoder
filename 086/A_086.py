def main():
    N = int(input())
    xy = [map(int,input().split()) for _ in range(N)]
    t,x,y=[list(i) for i in zip(*xy)]
           
    question(N,t,x,y)
    
def question(N,t,x,y):
    #print(N,t,x,y)
    count=0
    if ((abs(0-x[0])+abs(0-y[0]))%2==abs(0-t[0])%2 and x[0]+y[0]<=t[0]):
        if(N>=1):
            count+=1
    else:
        None
    #print(count)
    
    for i in range(N-1):
        if(((abs(x[i]-x[i+1])+abs(y[i]-y[i+1])))%2==abs(t[i]-t[i+1])%2 and abs(x[i]-x[i+1])+abs(y[i]-y[i+1])<=abs(t[i]-t[i+1])):
            count+=1
            #print(count)

    print("Yes") if count==N else print("No")
    
main()
