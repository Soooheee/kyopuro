import sys
sys.setrecursionlimit(1000000)

n = int(input())
child = [[] for i in range(n)]
for i in range(1, n):
    b = int(input())
    child[b-1].append(i)
def dfs(i) :
    if len(child[i]) == 0 :
        return 1 
    else :
        value = []
        for j in child[i] :
            value.append(dfs(j))
        return max(value) + min(value) + 1 
print(dfs(0))
