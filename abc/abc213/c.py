n = int(input())
a = list(map(int,input().split()))
b = dict(zip(a,[i for i in range(1,n+1)]))
a.sort(reverse=True)
for i in a:
  print(b[i])


