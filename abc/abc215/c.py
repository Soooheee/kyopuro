import itertools 
s, k = input().split()
k = int(k)
s = sorted(list(s))
ls = set([])
for i in itertools.permutations(s, len(s)) :
    t = "".join(i)
    if t not in ls :
        ls.add(t)
ls = list(ls)
ls.sort()
print(ls[k-1])


