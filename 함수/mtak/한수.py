import sys

def is_hansu(n):
    if len(str(n)) > 1:
        diff = int(str(n)[1]) - int(str(n)[0])
    else:
        return True
    for i in range(len(str(n)) - 1):
        if str(n)[i+ 1] != str(int(str(n)[i]) + diff):
            return False
    return True

n = int(sys.stdin.readline())
cnt = 0
for i in range(1,n + 1):
    if is_hansu(i) != False:
        cnt += 1
print(cnt)