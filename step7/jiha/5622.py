st = input()

nlist = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
cnt = 0
for s in st:
    for i in range(8):
        if s in nlist[i]:
            cnt += i + 3
            break
print(cnt)