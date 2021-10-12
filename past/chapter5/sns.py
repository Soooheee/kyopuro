n, q = map(int, input().split())
graph = [[False for i in range(n)] for j in range(n)]
s = [list(map(int, input().split())) for i in range(q)]
for i in range(q):
    if s[i][0] == 1 :
        a, b = s[i][1], s[i][2]
        a -= 1 
        b -= 1
        graph[a][b] = True 
    if s[i][0] == 2 :
        a = s[i][1]
        a -= 1 
        for j in range(n) :
            if graph[j][a] :
                graph[a][j] = True
    if s[i][0] == 3 :
        a = s[i][1]
        a -= 1 
        ls = []
        for j in range(n) :
            if graph[a][j] :
                for k in range(n):
                    if graph[j][k] and k != a :
                        ls.append(k)
        for j in ls :
            graph[a][j] = True  
for i in range(n):
    for j in range(n):
        if graph[i][j] :
            print("Y", end = "")
        else :
            print("N", end = "")
    print()