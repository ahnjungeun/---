# 이거 백트래킹 방법으로 다시 풀어보기!
# 공부해보기~

input()
n = list(map(int,input().split()))
l = list(map(int,input().split()))

o = []
for _ in range(l[0]):
    o.append('+')
for _ in range(l[1]):
    o.append('-')
for _ in range(l[2]):
    o.append('*')
for _ in range(l[3]):
    o.append('/')

from itertools import permutations as p

op = list(p(o))
m = 1e9+1
M = -1e9-1

for k in op:
    k = list(k)
    x = n[0]
    for a in n[1:]:
        i = k.pop(0)

        if i == '+':x = x+a
        elif i == '-':x = x-a
        elif i == '*':x = x*a
        elif i == '/':
            if x<0:
                x*=-1
                x = -(x//a)
            else:
                x = x//a

    m = min(m,x)
    M = max(M,x)

print(M)
print(m)