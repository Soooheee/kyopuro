p = int(input())
coin = [1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800]
coin.sort(reverse = True)
sumc = 0 

for i in range(10):
    if p == 0 :
        break
    if coin[i] <= p :
        num = p // coin[i]
        p -= num * coin[i]
        sumc += num 
print(sumc)
