a, b, x = map(int, input().split())
left = 0 
right = 10 ** 9 + 1
while right > left + 1 :
    mid = (right + left) // 2 
    d = len(str(mid))
    price = a * mid + b * d 
    if price <= x :
        left = mid 
    else :
        right = mid 
print(left)