n,s = map(int,input().split())
l = list(map(int,input().split()))

res = 0

def back(m,k):
    global res
    if len(arr)==m:
        # print(arr)
        ans = sum(arr)
        if ans == s:
            res+=1
        return
    
    for i in range(k,n):
        if i not in check:
            arr.append(l[i])
            check.append(i)
            back(m,i+1)
            arr.pop()
            check.pop()

for m in range(1,n+1):
    arr=[]
    check=[]
    back(m,0)

print(res)