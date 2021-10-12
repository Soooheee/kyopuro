n, m = map(int, input().split())
island = [[] for i in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    a -= 1 
    b -= 1 
    island[a].append(b)
    island[b].append(a)
for i in range(len(island[0])) :
    if n-1 in island[island[0][i]] :
        print("POSSIBLE")
        exit()
print("IMPOSSIBLE")