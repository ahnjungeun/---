n,m = map(int,input().split())
l = sorted(input().split())

res = set()
arr = []
def back():
    if len(arr)==n:
        for i in arr:
            if i in 'aeiou':
                res.add(''.join(sorted(arr)))
                break
        return
    for i in l:
        if i not in arr:
            # ^^ 시간초과 ^^
            # https://www.acmicpc.net/problem/1759
            arr.append(i)
            back()
            arr.pop()


back()
for i in sorted(res):
    print(i)