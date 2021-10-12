n = int(input())
x = [[] for i in range(n)]
for i in range(n):
    a, b = map(int, input().split())
    x[a-1].append(b)
cnt = [0] * 101 
ans = 0 
for d in range(n):
    for b in x[d] :
        cnt[b] += 1
    for b in range(100, 0, -1):
        if cnt[b] > 0 :
            ans += b 
            cnt[b] -= 1 
            break 
    print(ans)
    