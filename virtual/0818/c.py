t, n = map(int, input().split())
a = 100 // t 
b = 100 % t 
count = 0 
if  b == 0 :
    cnt = -1
elif t % b == 0 :
    cnt = t // b 
else :
    cnt = t // b + 1 
ans = 0 
for i in range(1, n+1):
    if ans == cnt :
        count += 1 
        ans = 0 
    if b == 0 :
        count += a 
    else :
        count += (a + 1)
    ans += 1 
print(count)
