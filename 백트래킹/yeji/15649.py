#[15649]백트래킹, N과 M(1)
#1부터 N까지 자연수 중에서 중복 없이 길이가 M개인 수열 출력
#백트래킹(Backtracking, 퇴각검색)

n,m = list(map(int,input().split()))
s = []
def dfs():
    if len(s)==m:
        print(' '.join(map(str,s)))
        return
    
    for i in range(1,n+1):
        if i not in s:
            s.append(i)
            dfs()
            s.pop()
dfs()