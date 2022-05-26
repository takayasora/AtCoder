N=int(input())
listA = list(map(int,input().split(" ")))

count=0
while(1):
    list_hantei = [listA[k] % 2 == 0 for k in range(len(listA))]
    if(sum(list_hantei)==N):
        count+=1
        listB = [listA[j] / 2 for j in range(len(listA))]
        listA = listB
    else:
        break

print(count)
