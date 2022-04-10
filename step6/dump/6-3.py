#1065 한수
#한수: 양의 정수의 각 자리가 등차수열(연속된 두 개의 수 차이가 일정)을 이루는 수
#1보다 크거나 같고, N보다 작거나 같은 한수의 개수를 출력

def hansu(num) :
    hansu_cnt = 0
    for i in range(1, num+1):
        num_list = list(map(int,str(i)))
        if i < 100:
            hansu_cnt += 1  # 100보다 작으면 모두 한수
        elif num_list[0]-num_list[1] == num_list[1]-num_list[2]:
            hansu_cnt += 1  # x의 각 자리가 등차수열이면 한수
    return hansu_cnt

num = int(input())
print(hansu(num))