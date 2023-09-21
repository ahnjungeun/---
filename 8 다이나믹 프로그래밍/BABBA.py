# https://www.acmicpc.net/problem/9625
n=int(input())+1
d = [(1,0)]*n

for i in range(1,n):
    d[i] = (d[i-1][1],sum(d[i-1]))

print(*d[-1])

# 오 디피래서 테이블 선언했는데
a,b = 1,0
for i in range(n):
    a,b = b,a+b
# 로 풀 수 있구나! 오...
# 값을 저장해서 구하니까 dp인 건가?
# 옛날에는다 문자열 바꿔서  count 했는데ㅋㅋ
# 아직까지는 알고리즘 유형보고 풀지만
# 언젠가는 꼭! 무슨 유형인지 스스로 알아내겠어