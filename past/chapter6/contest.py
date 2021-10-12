n = int(input())
ps = [0] + list(map(int, input().split()))
P = sum(ps)
dp = [[False for i in range(P+1)] for j in range(n+1)]
dp[0][0] = True 
for i in range(1, n+1):
    for j in range(P+1):
        if dp[i-1][j] :
            dp[i][j] = True 
        if j >= ps[i] and dp[i-1][j-ps[i]]:
            dp[i][j] = True 
ans = 0 
for i in range(P+1):
    if dp[n][i] :
        ans += 1 
print(ans)
