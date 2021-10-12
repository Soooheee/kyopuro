s = input()
cnt = 0 
for i in range(len(s)- 3):
    if s[i] == "Z" and s[i+1] == "O" and s[i+2] == "N" and s[i+3] == "e" :
        cnt += 1 
print(cnt)
