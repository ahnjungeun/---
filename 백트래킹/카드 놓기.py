n = int(input())
k = int(input())

l=[]
res=set()

for i in range(n):
    l.append((int(input()),i))

arr=[]
check=[]
def back():
    if len(arr)==k:
        ans = int(''.join(map(str,arr)))
        res.add(ans)
        return
    
    for v,i in l:
        if i not in check:
            arr.append(v)
            check.append(i)
            back()
            arr.pop()
            check.pop()

back()
print(len(res))