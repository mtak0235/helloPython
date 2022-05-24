import sys

answer = 0
input = sys.stdin.readline
def group_word_checker(str):
    group = set()
    pre = str[0]
    group.add(pre)
    for s in str[1:]:
        if s == pre: continue
        if s in group: return
        pre = s
        group.add(s)
    global answer
    answer += 1
        

N = int(input())
for _ in range(N):
    group_word_checker(input())

print(answer)

# 정렬의 key를 활용
def checker_lambda(str):
    if str == sorted(str, key=str.find): return 1
    return 0
