def self_num_gen():
    def d(n):
        ret = n
        while n:
            ret += n % 10
            n //= 10
        return ret

    i = 1
    non_self_nums = set()
    while True:
        if i not in non_self_nums:
            yield i
        else:
            non_self_nums.remove(i)
        non_self_nums.add(d(i))
        i += 1

g = self_num_gen()
n = next(g)
while n < 10000:
    print(n)
    n = next(g)
