n = int(input())
r = input()
cnt = 0 
for i in range(n):
    if r[i] == "A" :
        cnt += 4 
    elif r[i] == "B" :
        cnt += 3 
    elif r[i] == "C" :
        cnt += 2 
    elif r[i] == "D" :
        cnt += 1 
print(cnt / n)

