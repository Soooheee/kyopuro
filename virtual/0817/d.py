q, h, s, d = map(int, input().split())
n = int(input())
a = min(q * 4 , h * 2 ,s)
b = min(q * 8 , h * 4 , s * 2 , d)
x = n // 2
y = n % 2
ans = x * b + y * a
print(ans)


