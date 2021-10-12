import sys 
sys.setrecursionlimit(1000000)

n, m = map(int, input().split())
edge = [[] for i in range(n)]
indeg = [0] * n 
for i in range(m):
    x, y = map(int, input().split())
    edge[x-1].append(y-1)
    indeg[y-1] += 1 
length = [0] * n 
done = [False] * n 

def rec(i) :
    if done[i] :
        return length[i]
    length[i] = 0 
    for j in edge[i] :
        length[i] = max(length[i], rec(j) + 1)
    done[i] = True 
    return length[i]

for i in range(n):
    if indeg[i] == 0 :
        rec(i)
print(max(length))