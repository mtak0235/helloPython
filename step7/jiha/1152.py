""" st = input()

cnt = 1
tf = False
for s in st:
    if s == ' ' and tf:
        cnt += 1
    elif s != ' ':
        tf = True
if s[-1] == ' ':
    cnt -= 1

print(cnt) """
# 파이썬 사랑합니다
st = list(input().split())
print(len(st))