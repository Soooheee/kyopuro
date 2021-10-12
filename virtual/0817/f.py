from collections import deque
s = deque()
t = input()
rev = False
for i in t:
    if i == 'R':
        rev = not rev
    elif rev:
        if s and s[0] == i:
            s.popleft()
        else:
            s.appendleft(i)
    else:
        if s and s[-1] == i:
            s.pop()
        else:
            s.append(i)
if rev:
    s = reversed(s)
print("".join(s))

