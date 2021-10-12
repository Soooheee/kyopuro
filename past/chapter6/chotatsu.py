n, m = map(int, input().split())
S = [0]
C = [0]
for i in range(m):
    s, c = input().split()
    s_val = 0 
    for j in range(n):
        if s[j] == "Y":
            s_val |= 1 << j 
    S.append(s_val)
    C.append(int(c))
all = 1 << n 
INF = 10 ** 100 
cost = [[INF for i in range(all)] for j in range(m+1)]
cost[0][0] = 0 
for i in range(1, m + 1):
    for j in range(all) :
        cost[i][j] = min(cost[i][j], cost[i-1][j])
        cost[i][j|S[i]] = min(cost[i][j|S[i]], cost[i-1][j] + C[i])
ans = cost[m][all - 1]
if ans == INF :
    ans = -1 
print(ans)