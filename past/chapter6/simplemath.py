a, b, c = map(int, input().split())
d = (a+1)*a//2 
e = (b+1)*b//2
f = (c+1)*c//2
print(d * e * f % 998244353)
