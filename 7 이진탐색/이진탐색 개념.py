target = 47

def bin(arr,target,s,e):
    while s<=e:
        m = (s+e)//2
        if arr[m] == target:
            return m
        elif arr[m] > target:
            e = m-1
        else:
            s = m+1
    return -1

arr = range(24,62)
res = bin(arr,target,0,len(arr)-1)

# 인덱스 0부터 시작
print(res)