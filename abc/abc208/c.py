n, k = map(int,input().split())
a = list(map(int, input().split()))
ls = []
for i in range(n):
  ls.append((a[i], i))
b = k//n
ls.sort()
C = [0] * n
 
for i in range(k % n):
    C[ls[i][1]] += 1
for i in range(n):
    print(C[i] + b)