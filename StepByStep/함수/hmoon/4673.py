def selfnumber(num, cnt):
    ret = num
    temp = num
    num = list(map(int, str(num)))
    for nums in num:
        ret += nums
    cnt += 1
    if (ret > 10000 and cnt == 1):
        return (-2)
    if (ret > 10000):
        return (-1)
    if ret != temp:
        nlist.append(ret)
    return (selfnumber(ret, cnt))

if __name__ == "__main__":
    nlist = []
    n = 1
    while (1):
        cnt = 0
        ret = selfnumber(n, cnt)
        if (ret == -1):
            n += 1
        if (ret == -2):
            break
    nlist = set(nlist)
    nlist = list(nlist)
    nlist.sort()
    for i in range(1, 9997):
        if i not in nlist:
            print(i)
