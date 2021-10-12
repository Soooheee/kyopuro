n = int(input())
arr = []
for i in range(n):
    a, b = map(int, input().split())
    arr.append([-a-b, a, b])
arr.sort()
ans = 0 
for i in range(n):
    c, a, b = arr[i]
    if i % 2 == 0 :
        ans += a 
    else :
        ans -= b 
print(ans)
