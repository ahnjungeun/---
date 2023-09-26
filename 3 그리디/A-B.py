a,b = map(int,input().split())
c=1
while 1:
    if b%2==0:
        b/=2
        # print(b)
    elif b%10==1:
        b//=10
        # print(b)
    else:
        print(-1)
        break
    c+=1
    if a==b:
        print(c)
        break
    elif b<a:
        print(-1)
        break

# 당신은 나의 천사~
# https://www.acmicpc.net/board/view/109295
# bfs로 푸는 건 다음에 알아보기~