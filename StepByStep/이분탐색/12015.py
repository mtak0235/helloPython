import sys,bisect
N = int(sys.stdin.readline())
A = [int(x) for x in sys.stdin.readline().split()]
ans = [0]

for i in A:
    if ans[-1] < i:
        ans.append(i)
    else:
        ans[bisect.bisect_left(ans,i)] = i

print(len(ans)-1)
