#[11720]step7,숫자의 합

n = int(input()) #숫자의 개수
n_list = list(input()) #입력받은 숫자
sum = 0

for i in range (n):
    sum += int(n_list[i])
print(sum)

# n = input()
# print(sum(map(int,input())))