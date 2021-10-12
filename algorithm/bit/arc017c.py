from collections import defaultdict 
n, x = map(int, input().split())
a = []
b = []
for i in range(n):
    w = int(input())
    if i % 2 == 0 :
        a.append(w)
    else :
        b.append(w)
def has_bit(nn, i):
    return (nn & (1 << i) > 0)
dic = defaultdict(int)
for nn in range(1 << len(b)) : 
    s = 0 
    for i in range(n):
        if has_bit(nn, i) :
            s += b[i]
    dic[s] += 1
ans = 0 
for nn in range(1 << len(a)):
    s = 0 
    for i in range(n) :
        if has_bit(nn, i) :
            s += a[i]
    ans += dic[x - s]
print(ans)
