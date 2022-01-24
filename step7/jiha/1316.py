# 교훈 : 슬라이싱을 잘 활용하자
n = int(input())

count = 0
for _ in range(n):
    st = input()
    check = True
    for i in range(len(st) - 1):
        if st[i] == st[i + 1]:
            continue
        elif st[i] in st[i + 1 :]:
            check = False
            break
    if check:
        count += 1

print(count)