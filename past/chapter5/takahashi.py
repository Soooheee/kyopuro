c = [list(map(int, input().split())) for i in range(3)]
h = 0
w = 0 
for i in range(3):
    for j in range(3):
        if i == j :
            h += c[i][j]
        w += c[i][j]
if h * 3 == w:
    print("Yes")
else :
    print("No")
