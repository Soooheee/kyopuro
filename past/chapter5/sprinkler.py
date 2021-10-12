n, m, q = map(int, input().split())
UV = [list(map(lambda x:int(x)-1, input().split())) for i in range(m)]
c = list(map(int, input().split()))
s = [list(map(int, input().split())) for i in range(q)]
graph = [[] for i in range(n)]
for i in range(m):
    graph[UV[i][0]].append(UV[i][1])
    graph[UV[i][1]].append(UV[i][0])

for i in range(q) :
    if s[i][0] == 1 :
        num = s[i][1] - 1 
        print(c[num])
        for j in range(len(graph[num])):
            c[graph[num][j]] = c[num]
    if s[i][0] == 2 :
        num = s[i][1] - 1 
        print(c[num]) 
        c[num] = s[i][2]


