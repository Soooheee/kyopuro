n, w = map(int, input().split())
wv = [list(map(int, input().split())) for i in range(n)]
dp = [[-10**18 for i in range(w+1)] for i in range(n+1)]
dp[0][0] = 0 
for i in range(n):
    for j in range(w+1) :
        dp[i+1][j] = max(dp[i][j], dp[i+1][j])
        if j - wv[i][0] >= 0 :
            dp[i+1][j] = max(dp[i+1][j], dp[i][j-wv[i][0]] + wv[i][1])
print(dp[n][w])
