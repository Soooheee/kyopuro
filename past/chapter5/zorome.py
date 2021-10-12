n = int(input())
sho = n // 9 
res = n % 9 
print(str(res) * (sho + 1) if res != 0 else "9" * (sho))  