a = int(input())
b = input()

for i in range(0, len(b)):
    print(a * int(b[len(b)-i-1]))
print(a*int(b))