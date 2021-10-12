n = int(input())
a = list(map(int, input().split()))
suma = sum(a)
cnt = 0 
diff = 2 * (10 ** 9) + 1
for i in range(n-1):
    cnt += a[i]
    sa = suma - cnt
    diff = min(diff, abs(sa - cnt)) 
print(diff)



