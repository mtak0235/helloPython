# 연산자 끼워넣기
n = int(input()) # n개의 수
a_list = list(map(int, input().split())) # 순열 a_list
op = list(map(int, input().split())) # 연산자(+, -, *, /) 개수

def dfs(depth, num):
  global min_num
  global max_num
  if depth == n:
    max_num = max(num, max_num)
    min_num = min(num, min_num)
    return
  else:
    for i in range(4):
      if op[i] > 0: # 연산자가 있으면
        op[i] -= 1 # 하나 사용
        if i == 0: # 연산자가 +일때
          dfs(depth+1, num+a_list[depth])
        elif i == 1: # 연산자가 -일때
           dfs(depth+1, num-a_list[depth])
        elif i == 2: # 연산자가 *일때
          dfs(depth+1, num*a_list[depth])
        elif i == 3: # 연산자가 /일때
          dfs(depth+1, int(num/a_list[depth]))
        op[i] += 1 # 개수 다시 돌려놓기

min_num = 1e9
max_num = -1e9
dfs(1, a_list[0])
print(max_num)
print(min_num)