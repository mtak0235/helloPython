import sys

def selfnumber(num, nlist):
    ret = num
    num_list = list(map(int, str(num)))
    for each_num in num_list:
        ret += each_num
    if (ret > 10000):
        return
    try:
        nlist.remove(ret)
    except:
        return
    return (selfnumber(ret, nlist))

if __name__ == "__main__":
    nlist = list(range(1, 10001))
    for num in range(1, 10001):
        ret = selfnumber(num, nlist)
    print(*nlist, sep='\n')
