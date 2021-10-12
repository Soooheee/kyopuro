n = int(input())
left = 0
right = n + 1

while right > left + 1:
    middle = (right + left) // 2 
    if (middle * (middle + 1) // 2 <= n+1 ):
        left = middle
    else:
        right = middle

print(n-left+1)

    
    