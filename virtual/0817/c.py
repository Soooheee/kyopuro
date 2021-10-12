y = int(input())
m = int(input())
d = int(input())
if m == 1 or m == 2 :
    y -= 1 
    m += 12
after = 365 * 2014 + int(2014/4) - int(2014/100) + int(2014/400) + int(306*(5+1)/10) + 17 - 429 
before = 365 * y + int(y/4) - int(y/100) + int(y/400) + int(306*(m+1)/10) + d - 429
print(after - before)