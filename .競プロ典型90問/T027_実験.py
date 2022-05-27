mydict = {"apple":1, "orange":2, "banana":3}

#出力
print(mydict)
print(mydict["apple"])

#存在チェック
print("apple" in mydict.keys())
print(3 in mydict.values())
print("sample" in mydict.keys())
print(5 in mydict.values())

#追加
mydict["peach"] = 4
print(mydict)
"""
mydict.update("peach"=3,"apple"=2)
"""
#変更
mydict["peach"] = 5
#削除
mydict.pop("orange")

#ソート
sortedDict = sorted(mydict.items())
print(sortedDict)#返り値がリスト型




"""
from collections import defaultdict

d=defaultdict(bool)

N=int(input())

for i in range(N):
    s=input()
    #print(d)
    if d[s]:
        continue
    d[s]=True
    print(i+1)
"""
