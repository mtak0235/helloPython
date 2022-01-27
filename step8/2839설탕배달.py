# 1 ---------------------------------------------
n = int(input())
count = n // 5

if n % 5 == 0:
    n = 0
else:
    for i in range(count, -1, -1):
        tmp = n - 5 * i
        if tmp % 3 == 0:
            count = i + (tmp // 3)
            n = 0
            break

if n == 0:
    print(count)
else:
    print(-1)

# 2 ---------------------------------------------
# sugar = int(input())

# bag = 0
# while sugar >= 0 :
#     if sugar % 5 == 0 :  # 5의 배수이면
#         bag += (sugar // 5)  # 5로 나눈 몫을 구해야 정수가 됨
#         print(bag)
#         break
#     sugar -= 3  
#     bag += 1  # 5의 배수가 될 때까지 설탕-3, 봉지+1
# else :
#     print(-1)