a, b, c, x, y = map(int, input().split())
s1 = a * x + b * y 
s2 = c * 2 * min(x, y)
s3 = c * 2 * max(x, y)
if x >= y :
    s2 += a * (x - y)
else :
    s2 += b * (y - x)
print(min(s1, min(s2, s3)))
