d = [1,1,1]
for i in range(3,101):
    d.append(d[i-2]+d[i-3])

for _ in range(int(input())):
    n = int(input())
    print(d[n-1])