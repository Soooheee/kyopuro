n = int(input())
a = list(map(int,input().split()))
cnt = 0
for i in range(n) :
  if a[i] % 2 == 0 :
    while a[i] % 2 == 0 :
      a[i] //= 2
      cnt += 1
print(cnt) 