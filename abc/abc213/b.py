n = int(input())
a = list(map(int, input().split()))
A = sorted(a)
num = A[-2]
for i in range(n) :
    if a[i]== num :
        print(i + 1)
        exit()
