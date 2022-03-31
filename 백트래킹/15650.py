#[15650]백트래킹, N과 M(2)
#N까지 자연수 중에서 중복 없이 M개를 고름, 오름차순

n,m = list(map(int,input().split()))
s = []
def dfs(start):
    if len(s)==m:
        print(' '.join(map(str,s)))
        return
    
    for i in range(start,n+1):
        if i not in s:
            s.append(i)
            dfs(i+1)
            s.pop()
dfs(1)