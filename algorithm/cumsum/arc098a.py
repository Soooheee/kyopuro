n = int(input())
s = input()
min_turn = 3 * 10 ** 5 
sum_w = [0]
for i in range(n):
    if s[i] == "W" :
        sum_w.append(sum_w[i] + 1)
    else :
        sum_w.append(sum_w[i])
for i in range(n):
    w = sum_w[i] 
    e = (n - 1- i) - (sum_w[n] - sum_w[i + 1])
    turn = w + e 
    min_turn = min(turn, min_turn)
print(min_turn)
