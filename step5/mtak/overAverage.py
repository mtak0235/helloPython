import sys
_class_cnt = int(sys.stdin.readline())
_avg = [0 for i in range(_class_cnt)]
_grades =[]
for i in range(_class_cnt):
    tmp = list(map(int, sys.stdin.readline().split()))
    _students = tmp.pop(0)
    _grades.append(tmp)
    for j in _grades[i]:
        _avg[i] += j
    _avg[i] /= _students
for i in range(len(_grades)):
    _over_avg = 0
    for j in _grades[i]:
        if j > _avg[i]:
            _over_avg += 1
    print("{0:0.3f}%".format(_over_avg/len(_grades[i]) * 100))