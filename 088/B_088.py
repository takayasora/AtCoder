N = input()
Alist = list(map(int,input().split()))
sort_Alist = sorted(Alist,reverse=True)
#print(sort_Alist)
Blist = [sort_Alist[i] if i%2==0 else -sort_Alist[i] for i in range(len(sort_Alist))]
print(sum(Blist))
