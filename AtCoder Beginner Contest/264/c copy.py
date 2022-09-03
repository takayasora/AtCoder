#入力値の読み込み
Ha,Wa=list(map(int,input().split()))
Alist=[]
for i in range(Ha):
    templist=[]
    templist=list(map(int,input().split()))
    Alist.append(templist)

Hb,Wb=list(map(int,input().split()))
Blist=[]
for i in range(Hb):
    templist=[]
    templist=list(map(int,input().split()))
    Blist.append(templist)

#print(Alist)
#print(Blist)


#全部がAlistのどこに配置されているかを数値化して新たな配列を作る
#

#numpy配列に変換
import numpy as np

arr_Alist=np.array(Alist)
arr_Blist=np.array(Blist)

