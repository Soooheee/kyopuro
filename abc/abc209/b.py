n, x = map(int, input().split())
a = list(map(int, input().split()))
cnt = 0
for i in range(n):
    if i % 2 == 1 :
        cnt += a[i]-1
    else :
        cnt += a[i]
print("Yes" if cnt <= x else "No") 