def sum4each_position(n):
    if n < 10:
        return n
    return (n%10) + sum4each_position(n//10)

def self_num():
    s1 = set(range(1,10001))
    s2 = set()
    [s2.add(i + sum4each_position(i)) for i in range(1, 10001)]
    ret = sorted(s1 - s2)
    [print(i) for i in ret]

self_num()