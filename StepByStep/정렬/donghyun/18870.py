l = list(map(int, list(open(0))[1].split()))
d = {v:k for k, v in enumerate(sorted(set(l)))}
print(*[d[i] for i in l])