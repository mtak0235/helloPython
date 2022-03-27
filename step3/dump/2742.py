import sys

N = int(sys.stdin.readline())

#range의 step 바꾸기
#range의 3번째 매개변수에 -1을 넣으면 내림차순으로 리스트를 가진다.
for i in range(N, 0, -1):
    print("%d" %(i))

# # reversed 써보기!
# # reversed()는 리스트의 원소를 거꾸로 뒤집고 반환한다.
# for i in reversed(range(1, N + 1)):
#     print("%d" %(i))