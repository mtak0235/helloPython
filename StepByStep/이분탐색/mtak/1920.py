import sys
input = sys.stdin.readline
n = int(input())
a = sorted(list(map(int, input().split())))
m = int(input())
b = list(map(int, input().split()))
def binarySearch(i):
    start = 0
    end = n - 1
    mid = (start + end) // 2
    while end - start  >= 0:
        if a[mid] == i:
            return mid
        elif a[mid] < i:
            start = mid + 1
        else:
            end = mid - 1
        mid = (start + end) // 2
    return -1
            
for i in b:
    if binarySearch(i) != -1:
        print(1)
        continue
    print(0)
