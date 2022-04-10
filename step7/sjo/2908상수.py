# 1 ---------------------------------------------
a, b = map(list, input().split())

tmp = a[0]
a[0] = a[2]
a[2] = tmp

tmp = b[0]
b[0] = b[2]
b[2] = tmp

num_a = 100 * int(a[0]) + 10 * int(a[1]) + int(a[2])
num_b = 100 * int(b[0]) + 10 * int(b[1]) + int(b[2])

print(max(num_a, num_b))

# 2 ---------------------------------------------
# a, b = input().split()
# a = int(a[::-1])
# b = int(b[::-1])

# if a > b:
#     print(a)
# else :
#     print(b)