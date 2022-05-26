def main():
    N,Y = map(int,input().split())
    question(N,Y)
    
def question(N,Y):
    for i in range(N+1):
        for j in range(N-i+1):
            k=N-i-j
            total=i*10000 + j*5000 + k*1000
            if(total==Y):
                print(str(i)+" "+str(j)+" "+str(N-i-j))
                return()

    print("-1 -1 -1")

main()
