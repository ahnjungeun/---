s = input()

l = len(s)//2
s1,s2 = s[:l],s[l:]
r1,r2 = 0,0

for i in range(l):
    r1 += int(s1[i])
    r2 += int(s2[i])

if r1==r2:
    print('LUCKY')
else:
    print('READY')



# -------- 노트 --------

# 문자열로 들어온 숫자를 바로 int로 변환해서 리스트에 저장하기
s = [*map(int,input())] # 입력 7755 결과 [7,7,5,5]

# sum()을 이용해서 구하기
# 위와 같이 s를 받아야 사용가능
sum(s[:l]) == sum(s[l:])