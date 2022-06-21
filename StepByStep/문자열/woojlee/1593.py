# 문자열, 슬라이딩 윈도우
# 문자 해독

import sys

g, S_len = map(int, sys.stdin.readline().split())
W = sys.stdin.readline()
S = sys.stdin.readline()

W_cnt = [0] * (122 - 65 + 1) # ASCII 'A' ~ 'z'까지 
S_cnt = [0] * (122 - 65 + 1)

for w in range(g):
    w_idx = ord(W[w]) - 65
    W_cnt[w_idx] += 1


answer = 0
head = 0
for s in range(S_len):
    s_idx = ord(S[s]) - 65
    S_cnt[s_idx] += 1

    if s - head + 1 == g:
        if W_cnt == S_cnt:
            answer += 1
        # 슬라이딩 윈도우
        S_cnt[ord(S[head]) - 65] -= 1
        head += 1
    
print(answer)