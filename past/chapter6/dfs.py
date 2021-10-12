import sys 
sys.setrecursionlimit(1000000)
h, w = list(map(int, input().split()))
s = [input() for i in range(h)]
for i in range(h):
    for j in range(w):
        if s[i][j] == "s":
            si, sj = i, j 
        if s[i][j] == "g":
            gi, gj = i, j 
visited = [[False for i in range(w)] for j in range(h)]
def dfs(i, j):
    visited[i][j] = True 
    for i2, j2 in [[i+1, j], [i-1, j], [i, j+1], [i, j-1]] :
        if not (0 <= i2 < h and 0 <= j2 < w ) :
            continue 
        if s[i][j] == "#":
            continue 
        if not visited[i2][j2]:
            dfs(i2, j2)
dfs(si, sj)
if visited[gi][gj]:
    print("Yes")
else :
    print("No")