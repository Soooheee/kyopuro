a, b = map(int, input().split())
diff = b - a 
for i in range(diff, 0, -1):
    cnt = 0 
    p = b // diff 
    for j in range(1, p + 1) :
        if a <= i * j <= b :
            cnt += 1 
    if cnt == 2 :
        print(i)
        exit()
print(1)
