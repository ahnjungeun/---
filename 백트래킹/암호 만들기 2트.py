n,m = map(int,input().split())
l = sorted(input().split())

from itertools import combinations
vowel = 'aeiou'

for i in combinations(l,n):
    c=0
    for j in i:
        if j in vowel:
            c+=1

    if c>0 and n-c>1:
        print(''.join(i))