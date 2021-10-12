n, m = map(int, input().split())
a = list(map(int, input().split()))
bl = [False] * (m+1) 
def primes(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = False
    is_prime[1] = False
    for i in range(2, int(n**0.5) + 1):
        if not is_prime[i]:
            continue
        for j in range(i * 2, n + 1, i):
            is_prime[j] = False
    return [i for i in range(n + 1) if is_prime[i]]
def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a
prime_num = len(primes(m)) + 1
prime_ls = [1] + primes(m)
for i in prime_ls:
    bl[i] = True 

for i in range(n) :
    A = prime_factorize(a[i])
    for j in A :
        if bl[j] == True :
            prime_num -= 1 
            bl[j] = False  
print(prime_num) 
for i in prime_ls :
    if bl[i] == True :
        print(i)




