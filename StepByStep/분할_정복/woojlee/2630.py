# 색종이 만들기
# 분할 정복

import sys

input = sys.stdin.readline

def divided_check(arr, n):
    if n == 1:
        return True
    flag = arr[0][0]
    for i in range(n):
        for j in range(n):
            if arr[i][j] is not flag:
                return False
    return True

def divide(arr, n):
    if divided_check(arr, n):
        if arr[0][0] == '1':
            global blue
            blue += 1
        else:
            global white
            white += 1
        return
    arr1 = []
    arr2 = []
    arr3 = []
    arr4 = []
    harf_n = n // 2
    for i in range(n):
        arr1.append(arr[i][:harf_n])
        arr2.append(arr[i][harf_n:])
    for i in range(harf_n, n):
        arr3.append(arr[i][:harf_n])
        arr4.append(arr[i][harf_n:])
    divide(arr1, harf_n)
    divide(arr2, harf_n)
    divide(arr3, harf_n)
    divide(arr4, harf_n)

N = int(input())
A = [input().split() for _ in range(N)]

blue, white = 0, 0
divide(A, N)

print(white)
print(blue)