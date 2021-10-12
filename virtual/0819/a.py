from collections import deque 
n = int(input())
a = set(list(map(int, input().split())))
a = sorted(list(a)) 
minn = min(a)
maxn = max(a)
while maxn != minn :
    a = deque(a)
    a.append(maxn - minn)
    a = set(a)
    minn = min(a)
    maxn = max(a)
print(minn)

