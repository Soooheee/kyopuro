e = list(map(int, input().split()))
b = int(input())
l = list(map(int, input().split()))
flag = False 
cnt = 0 
for i in range(len(e)) :
    if l[i] in e :
        cnt += 1 
    else :
        if l[i] ==  b :
            flag = True 
if cnt == 5 :
    if flag :
        print(2)
    else :
        print(3)
else :
    if cnt ==  6 :
        print(1)
    elif cnt == 4 :
        print(4)
    elif cnt == 3 :
        print(5)
    else :
        print(0) 
    
    
            

