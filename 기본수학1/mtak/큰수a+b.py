import sys
def reverse(s):
    tmp = list()
    for i in range(len(s)):
        tmp.insert(0, s[i])
    s = ""
    for c in tmp:
        s += str(c)
    return s
a, b = map(str,sys.stdin.readline().split())
a = reverse(a)
b = reverse(b)
if len(a) > len(b):
    for i in range(len(a) - len(b)):
        b = b + "0"
else:
    for i in range(len(b) - len(a)):
        a = a + "0"
ev = 0
res = list()
for i in range(len(a) + 1) :
    res.append(0)
for i in range(len(a)):
    t = ord(a[i]) - ord('0')  + ord(b[i]) - ord('0') + ev
    if t < 0: t += ord('0')
    if t > 9: ev = 1
    else: ev = 0
    res[i] = chr( t%10 + ord("0"))
if ev == 1:
    res[len(a)] = "1"
_str = ""
for i in res:
    if i == 0:
        break
    _str = _str + i
print(reverse(_str))
