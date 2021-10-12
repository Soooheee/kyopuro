n = int(input())
c = list(map(int, input().split()))
q = int(input())
sell = 0 
z = 0 
s = 0 
min_s = 10 ** 9 
min_z = 10 ** 9 
for i in range(n):
    if i % 2 == 0 :
        min_s = min(c[i], min_s)
    else :
        min_z = min(c[i], min_z)
for i in range(q):
    query = list(map(int, input().split()))
    if query[0] == 1 :
        x = query[1] - 1
        a = query[2]
        if x % 2 == 0 :
            card = c[x] - z - s 
        else :
            card = c[x] - z 
        if card >= a :
            c[x] -= a 
            sell += a 
            if x % 2 == 0 :
                min_s = min(c[x], min_s)
            else :
                min_z = min(c[x], min_z)
    elif query[0] == 2 :
        a = query[1]
        if min_s - s - z >= a :
            s += a 
    elif query[0] == 3 :
        a = query[1]
        if min(min_s - s - z, min_z - z) >= a :
            z += a 
for i in range(n):
    if i % 2 == 0 :
        sell += s 
sell += z * n 
print(sell)