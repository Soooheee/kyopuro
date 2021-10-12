n, k = map(int, input().split())
a = list(map(int, input().split()))
right = n 
left = -1
while right > left + 1 :
    mid = (right + left) // 2 
    if a[mid] >= k :
        right = mid 
    else :
        left = mid 
if right == n :
    print(-1)
else :
    print(right)
     