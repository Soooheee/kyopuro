n = int(input())
s = [list(input()) for i in range(n)] 
for i in range(n-2, -1, -1):
    for j in range(1, 2 * n - 2) :
        if s[i][j] == "#" and (s[i+1][j-1] == "X" or s[i+1][j] == "X" or s[i+1][j+1] == "X" ):
            s[i][j] = "X" 
for i in range(n) :
    print("".join(s[i]))