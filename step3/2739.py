import sys

N = int(sys.stdin.readline())

# # 리스트의 원소들을 모두 써보자
# def printTimesTable_list(N):
#     base = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#     if N >= 1 and N <= 9:
#         for i in base:
#             print("%d * %d = %d" %(N, i, N * i))
# printTimesTable_list(N)

# # range 를 써보자
# def printTimesTable(N):
#     if N >= 1 and N <= 9:
#         for i in range (1, 10):
#             print("%d * %d = %d" %(N, i, N * i))
# printTimesTable(N)

# range로 리스트 객체를 생성해보자
def printTimesTable_range(N):
    base = range(1, 10)
    if 1 <= N and N <= 9:
        for i in base:
            print("%d * %d = %d" %(N, i, N * i))       
printTimesTable_range(N)