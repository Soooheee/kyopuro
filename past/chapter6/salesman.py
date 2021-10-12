n = int(input())
a = [list(map(int, input().split())) for i in range(n)]
all = 1 << n 
INF = 10 ** 100 
cost = [[INF for i in range(n)] for j in range(all)]
cost[0][0] = 0 
def has_bit(nn, i) :
    return (nn & (1 << i) > 0)
for nn in range(all) :
    for i in range(n):
        for j in range(n):
            if has_bit(nn, j) or i == j :
                continue 
            cost[nn|(1<<j)][j] = min(cost[nn|(1<<j)][j], cost[nn][i] + a[i][j])
print(cost[all-1][0])
