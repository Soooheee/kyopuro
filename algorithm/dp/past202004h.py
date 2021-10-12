n, m = list(map(int, input().split()))
grid = [input() for i in range(n)]
group = [[] for i in range(11)]
for i in range(n):
    for j in range(m):
        if grid[i][j] == "S":
            a = 0 
        elif grid[i][j] == "G":
            a = 10 
        else :
            a = int(grid[i][j])
        group[a].append([i, j])
INF = 10 ** 100
cost = []
for i in range(n):
    cost.append([INF] * m)
si, sj = group[0][0]
cost[si][sj] = 0 
for N in range(1, 11):
    for i, j in group[N]:
        for i2, j2 in group[N-1]:
            cost[i][j] = min(cost[i][j], cost[i2][j2] + abs(i - i2) + abs(j - j2))
gi, gj = group[10][0]
ans = cost[gi][gj]
if ans == INF :
    ans = -1
print(ans)