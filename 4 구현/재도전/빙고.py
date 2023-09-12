l = [list(map(int,input().split())) for _ in range(5)]
s = [list(map(int,input().split())) for _ in range(5)]
f = True
c=k=0

for i in s:
    for j in i:
        k+=1
        c_sum = 0
        for a in range(5):
            for b in range(5):
                if l[a][b] == j:
                    l[a][b] = 0
                    print(k)
                    print(*l,sep='\n')
                    print()
                c_sum += l[b][a]
            if c_sum == 0:
                print('인생..')

        if c == 3:
            f = False
            break
    if not f:
        break
                
print(k)