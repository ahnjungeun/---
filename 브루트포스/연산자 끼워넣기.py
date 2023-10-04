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

# --------
# 시간초과 나서 pypy로 돌렸고 m,M가 +-1e9가 실수여서 출력조건에 안 맞는대
# 아직 최대최소 헷갈리네~ 파이팅!
# https://velog.io/@kimdukbae/BOJ-14888-%EC%97%B0%EC%82%B0%EC%9E%90-%EB%81%BC%EC%9B%8C%EB%84%A3%EA%B8%B0-Python