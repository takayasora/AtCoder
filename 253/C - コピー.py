Q=int(input())
def query_1(query_list,ans_list):
    ans_list.append(query_list[1])
    return ans_list
    
def query_2(query_list,ans_list,query_list_min,query_list_min_count):
    c=query_list[2]
    s_in_x=ans_list.count(query_list[1])

    if c<=s_in_x:
        min_num = query_list[2]
    else:
        min_num=ans_list.count(query_list[1])

    min_counter=query_list_min_count
    for k in range(min_num):
        #ans_list.remove(query_list[1])
        ans_list=ans_list.pop(query_list[1])
        print(ans_list)
        
    return ans_list

def query_3(query_list,ans_list):
    if(len(ans_list)!=0):
        print(max(ans_list)-min(ans_list))
        return ans_list
    else:
        return ans_list
    
min_counter=0
ans_list=[]
for i in range(Q):
    query_list=list(map(int,input().split()))
    if(query_list[0]==1):
        ans_list=query_1(query_list,ans_list)
    elif(query_list[0]==2):
        ans_list=query_2(query_list,ans_list,min(ans_list),ans_list.count(min(ans_list)))
    elif(query_list[0]==3):
        ans_list=query_3(query_list,ans_list)
