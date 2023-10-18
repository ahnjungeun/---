n = int(input())
item = sorted(list(map(int,input().split())))
m = int(int(input()))
find = list(map(int,input().split()))

def bin(arr,target,s,e):
    while s<=e:
        m = (s+e)//2
        if arr[m] == target:
            return 'yes'
        elif arr[m] > target:
            e = m-1
        else:
            s = m+1
    return 'no'

for i in find:
    ans = bin(item,i,0,n-1)
    print(ans,end=' ')