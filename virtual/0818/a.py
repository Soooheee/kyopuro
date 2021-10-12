n = int(input())
S = []
T = []
for i in range(n):
    s, t = input().split()
    S.append(s)
    t = int(t)
    T.append(t)
x = input()
flag = False 
cnt = 0
for i in range(n):
    if S[i] == x :
        flag = True 
        continue 
    if flag :
        cnt += T[i]
print(cnt)
