import sys
_num = int(sys.stdin.readline())
_students = list()
for i in range(_num):
    a, b = map(int, sys.stdin.readline().split())
    _students.append([a,b])
_rank = list()
for i in range(_num):
    _rank.append(1)
    for j in range(_num):
        if i == j: continue;
        _flag = 0
        for k in range(2):
            if _students[i][k] < _students[j][k]:
                _flag += 1
        if _flag == 2:
            _rank[i] += 1
for p in _rank:
    print(p, end=" ")
print()
        