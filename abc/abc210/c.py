from collections import defaultdict 
n, k = map(int, input().split())
c = list(map(int, input().split()))
#尺取り法実装
dd = defaultdict(int)
ans = 0 
cnt = 0 
for i in range(n):
    if dd[c[i]] == 0 :
        cnt += 1
    dd[c[i]] += 1 
    if i >= k :
        dd[c[i-k]] -= 1
        if dd[c[i-k]] == 0 :
            cnt -= 1
    ans = max(ans, cnt)
print(ans)