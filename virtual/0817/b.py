h, w = map(int, input().split())
grid = [list(input()) for i in range(h)]
cnt = 0 
for i in range(h):
    for j in range(w-1):
        if grid[i][j] == "." and grid[i][j+1] == ".":
            cnt += 1 
for i in range(h-1):
    for j in range(w):
        if grid[i][j] == "." and grid[i+1][j] == ".":
            cnt += 1
print(cnt)
        
