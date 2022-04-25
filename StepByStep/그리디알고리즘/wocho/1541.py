poly = input().strip()

# 양수는 참 음수는 거짓
sign = True
terms = []
lt = rt = 0
while rt < len(poly):
    while rt < len(poly) and poly[rt] != '-' and poly[rt] != '+':
        rt += 1
    if rt == len(poly):
        terms.append((int(poly[lt:rt]), sign))
    elif poly[rt] == '+':
        if lt != rt:
            terms.append((int(poly[lt:rt]), sign))
        sign = True
        lt = rt = rt + 1
    else:
        if lt != rt:
            terms.append((int(poly[lt:rt]), sign))
        sign = False
        lt = rt = rt + 1

i = 0
ans = 0
flag = False
while i < len(terms):
    if terms[i][1]:
        if flag:
            ans -= terms[i][0]
        else:
            ans += terms[i][0]
    else:
        ans -= terms[i][0]
        flag = True
    i += 1

print(ans)
