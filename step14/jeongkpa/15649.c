# N과 M

N, M = list(map(int,input().split()))

M_list = []

def func():
  if len(M_list) == M: #M_list 안에 리스트 갯수가 M개 인경우 (재귀 종료 조건)
    print(' '.join(map(str,M_list))) # 그때 안에 있는 M_list 출력
    return

  for i in range(1,N+1):
    if i in M_list:
        continue
    M_list.append(i)
    func()
    M_list.pop()

func()
