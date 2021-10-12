def is_match(t, s) :
    for i in range(0, len(s) - len(t) + 1):
        ok = True 
        for j in range(0, len(t)):
            if s[i+j] != t[j] and t[j] != "." :
                ok = False 
        if ok :
            return True 
    return False 
s = input()
c = "abcdefghijklmnopqrstuvwxyz."
m = []
for T in c :
    if is_match(T, s) :
        m.append(T)
for c1 in c:
    for c2 in c:
        T = c1 + c2 
        if is_match(T, s):
            m.append(T)
for c1 in c :
    for c2 in c :
        for c3 in c :
            T = c1 + c2 + c3 
            if is_match(T, s) :
                m.append(T)
print(len(m))
