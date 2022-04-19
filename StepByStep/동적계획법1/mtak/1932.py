import sys
input = sys.stdin.readline
_size = int(input())
_rectangle = [list(map(int, input().split())) for _ in range(_size)]
for i in range(1,_size):
    for j in range(i+1):
        if j == 0:
            _rectangle[i][j] = _rectangle[i][j] + _rectangle[i-1][j]
        elif i == j:
            _rectangle[i][j] = _rectangle[i][j] + _rectangle[i-1][j-1]
        else:
            _rectangle[i][j] = max(_rectangle[i][j]+_rectangle[i-1][j],
                               _rectangle[i][j]+_rectangle[i-1][j-1])

print(max(_rectangle[_size-1]))