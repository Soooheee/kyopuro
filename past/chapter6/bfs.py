from collections import deque 
r, c = list(map(int, input().split()))
sy, sx = list(map(int, input().split()))
gy, gx = list(map(int, input().split()))
s = [input() for i in range(r)]
sy -= 1 
sx -= 1 
gy -= 1
gx -= 1
dist = [[-1] * c for i in range(r)]
que = deque()
que.append([sy, sx])
dist[sy][sx] = 0 
while len(que) > 0 :
    i, j = que.popleft()
    for i2, j2 in [[i+1, j], [i-1, j], [i, j+1], [i, j-1]]:
        if not (0 <= i2 < r and 0 <= j2 < c):
            continue 
        if s[i][j] == "#":
            continue 
        if dist[i2][j2] == -1 :
            dist[i2][j2] = dist[i][j] + 1 
            que.append([i2, j2])
print(dist[gy][gx])

