# 이코테 부록 bisect 참고
# 고마워요 나동빈씨!

n = int(input())
l = sorted(map(int,input().split()))
m = int(input())
f = list(map(int,input().split()))

import bisect
def find(arr,target):
    left = bisect.bisect_left(arr,target)
    right = bisect.bisect_right(arr,target)
    return right - left

for i in f:
    print(find(l,i),end=' ')