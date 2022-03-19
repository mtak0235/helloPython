N,X = map(int,input().split())
N_list= list(map(int,input().split()))
ans = []
for i in N_list:
  if i < X:
    ans.append(i)
for a in range(len(ans)):
  print(ans[a], end=' ')