R, B = map(int, input().split())
x, y = map(int, input().split())
def check(i):
    r = R - i 
    b = B - i
    if r < 0 or b < 0 :
        return False 
    num = r // (x-1) + b //(y-1)
    return (num >= i)
left = 0 
right = 10 ** 18 + 1 
while right > left + 1 :
    mid = (right + left) // 2 
    if check(mid) :
        left = mid 
    else :
        right = mid 
print(left)
