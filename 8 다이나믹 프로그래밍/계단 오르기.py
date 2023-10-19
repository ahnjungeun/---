n = int(input())
l=[0]
for _ in range(n):
    l.append(int(input()))

dp = [[0,0] for _ in range(n+1)]
dp[1] = [l[1]]*2

for i in range(2,n+1):
    dp[i] = [dp[i-1][1]+l[i],max(dp[i-2])+l[i]]

print(max(dp[n]))