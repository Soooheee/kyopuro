def solve(a, r, n):
    if r == 1 :
        return a 
    for i in range(n-1):
        a *= r 
        if a > 10 ** 9 :
            return "large"
    return a 

a, r, n = map(int, input().split())
ans = solve(a, r, n)
print(ans)
