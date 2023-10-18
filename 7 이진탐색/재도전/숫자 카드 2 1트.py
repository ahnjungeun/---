# https://chancoding.tistory.com/45
# https://hongcoding.tistory.com/12
# 푸는 방법이 여러 개네;; 다 공부하자!

n = int(input())
l = sorted(map(int,input().split()))
m = int(input())
f = list(map(int,input().split()))

# 풀이 1 : 1초
count = {}
for i in l:
    if i in count:
        count[i]+=1
    else:
        count[i] = 1
for i in f:
    res = count.get(i)
    print(res if res else 0,end=' ')


# 풀이 2 : 1.5초
idx = 0
dic = {}

for i in sorted(f):
    c=0
    if i not in dic:
        while idx<len(l):
            if i == l[idx]:
                c+=1
                idx+=1
            elif i > l[idx]:
                idx+=1
            else:
                break
        dic[i] = c

for i in f:
    print(dic[i],end=' ')