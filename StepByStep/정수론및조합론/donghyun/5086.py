l=open(0).read().strip().split("\n")[:-1]
for i, j in map(str.split, l):
    i, j = int(i), int(j)
    if not i % j:
        print("multiple")
    elif not j % i:
        print("factor")
    else:
        print("neither")