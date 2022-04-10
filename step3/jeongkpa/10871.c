N,X = map(int,input().split())
num_list= list(map(int,input().split()))
ans = []
for i in num_list:
  if i < X:
    ans.append(i)
for a in range(len(ans)):
  print(ans[a], end=' ')