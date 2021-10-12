a, b, c, d = map(int, input().split())
suma = (a + b + c + d) / 2 
if a + b == suma or a + d == suma or a + c == suma or b + d == suma or c + b == suma or c + d == suma or a == suma or b == suma or c == suma or d == suma :
    print("Yes")
else :
    print("No")