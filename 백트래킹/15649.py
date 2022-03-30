#[15649]백트래킹, N과 M(1)
#1부터 N까지 자연수 중에서 중복 없이 길이가 M개인 수열 출력
#백트래킹(Backtracking, 퇴각검색)

n, m = map(int, input().split())

s = []
def f():
  if len(s) == m:
    print(' '.join(map(str, s)))
    return

  for i in range(1, n + 1):
    if i in s: #이미 선택한 숫자를 다시 선택하려 하면 배제
      continue
    s.append(i) #스택에 추가
    f() #동작
    s.pop() #다시 스택에서 빼내기

f()