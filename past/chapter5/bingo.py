a = [list(map(int, input().split())) for i in range(3)]
n = int(input())
b = [int(input()) for _ in range(n)]
g = [[False]* 3 for i in range(3)]

for i in range(n):
    num = b[i]
    for j in range(3):
        for k in range(3):
            if a[j][k] == num :
                g[j][k] = True 
for i in range(3):
    if g[i][0] and g[i][1] and g[i][2] : 
        print("Yes")
        exit()
for i in range(3):
    if g[0][i] and g[1][i] and g[2][i] : 
        print("Yes")
        exit()
if g[0][0] and g[1][1] and g[2][2] : 
    print("Yes")
    exit()
if g[0][2] and g[1][1] and g[2][0] :
    print("Yes")
    exit()
print("No")