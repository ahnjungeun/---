M = [list(map(int,input().split())) for _ in range(5)]
C = [list(map(int,input().split())) for _ in range(5)]
f = False
c=k=0

for i in C:
    for j in i:
        k+=1
        for a in range(5):
            for b in range(5):
                if M[a][b] == j:
                    M[a][b] = 0

                for z in range(5):
                    if sum(M[z])==0:
                        c+=1
                    if sum([x[z] for x in M])==0:
                        c+=1
                if M[0][0]+M[1][1]+M[2][2]+M[3][3]+M[4][4] == 0:
                    c+=1
                if M[4][0]+M[3][1]+M[2][2]+M[1][3]+M[0][4] == 0:
                    c+=1
                    
                if c >= 3:
                    f = True
                    break
                else:
                    c = 0
        if f:
            break
    if f:
        break
                
print(k)