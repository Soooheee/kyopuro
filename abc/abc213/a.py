a, b = map(int, input().split())
for i in range(10**6):
    if a ^ i == b :
        print(i)
        exit()
