# 네 번째 점
x_pos = []
y_pos = []
for _ in range(3):
  x, y = map(int, input().split())
  if x in x_pos:
    xx = x
  if y in y_pos:
    yy = y
  x_pos.append(x)
  y_pos.append(y)

for x in x_pos:
  if x != xx:
    x_ans = x
for y in y_pos:
  if y != yy:
    y_ans = y
print(x_ans, y_ans)

