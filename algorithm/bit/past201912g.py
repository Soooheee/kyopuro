n = int(input())
a = []
for i in range(n-1):
    ls = list(map(int, input().split()))
    a.append([0]*(i+1) + ls)
all = 1 << n 
happy = [0] * all 
def has_bit(nn, i) :
    return (nn & (1<<i) > 0 )
for nn in range(all):
    for i in range(n):
        for j in range(i+1, n):
            if has_bit(nn, i) and has_bit(nn, j) :
                happy[nn] += a[i][j]
ans = -10 ** 100 
for n1 in range(all):
    for n2 in range(all):
        if n1 & n2 > 0 :
            continue 
        n3 = all - 1 - (n1|n2) 
        ans = max(ans, happy[n1] + happy[n2] + happy[n3])
print(ans)

