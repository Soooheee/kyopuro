n = int(input())
ba = []
for i in range(n):
    a, b = list(map(int, input().split()))
    ba.append([b, a])
ba.sort()
ans = 0
last = 0 
for b, a in ba :
    if last < a :
        ans += 1 
        last = b 
print(ans)
