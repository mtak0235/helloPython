score = int(input())
_to = 100
_rank = ord('A')
while (_to - 10 > score) | (score > _to):
    if _to == 70:
        _rank = ord('F')
        break
    _rank += 1
    _to -= 10
print(chr(_rank))