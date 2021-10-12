n = int(input())
ans = 0 
for a in range(1, n):
    b = (n-1) // a 
    ans += b 
print(ans)
