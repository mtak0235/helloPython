#[15651]백트래킹, N과 M(3)

n,m = list(map(int,input().split()))
s = []
def dfs():
    if len(s)==m:
        print(' '.join(map(str,s)))
        return
    
    for i in range(1,n+1):
            s.append(i)
            dfs()
            s.pop()
dfs()