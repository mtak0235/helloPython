# import sys
# input = sys.stdin.readline
# density = int(input())
# side = [[] for _ in range(5)]
# for i in range(6):
#     d, v = map(int, input().split())
#     side[d].append([v, i])
# print(side)
# max_com = list()
# for i in [1, 3]:
#     if max(side[i]) > max(side[i + 1]):
#         max_com.append([i, side[i].index(max(side[i]))])
#     else:
#         max_com.append([i + 1, side[i + 1].index(max(side[i + 1]))])
# print(max_com)
# max_size = side[max_com[0][0]][max_com[0][1]][0] * side[max_com[1][0]][max_com[1][1]][0]
# w = 0
# h = 0
# if max_com[0][0] == 2:
#     if abs(side[max_com[0][0]][max_com[0][1]][1] - side[1][0][1]) > abs(side[max_com[0][0]][max_com[0][1]][1] - side[1][1][1]) :
#         w = side[1][1][1]
#     else:
#         w = side[1][0][0]
# if max_com[0][0] == 1:
#     if abs(side[max_com[0][0]][max_com[0][1]][1] - side[2][0][1]) > abs(side[max_com[0][0]][max_com[0][1]][1] - side[2][1][1]) :
#         w = side[2][1][1]
#     else:
#         w = side[2][0][0]
# if max_com[1][0] == 3:
#     if abs(side[max_com[0][0]][max_com[0][1]][1] - side[4][0][1]) > abs(side[max_com[0][0]][max_com[0][1]][1] - side[4][1][1]) :
#         h = side[4][1][1]
#     else:
#         h = side[4][0][0]
# if max_com[1][0] == 4:
#     if abs(side[max_com[0][0]][max_com[0][1]][1] - side[3][0][1]) > abs(side[max_com[0][0]][max_com[0][1]][1] - side[3][1][1]) :
#         h = side[3][1][1]
#     else:
#         h = side[3][0][0]
# inner_size = w * h
# print(w, h)
# # print((max_size - inner_size) *density)

K = int(input())
max_height = 0  # 가장 긴 높이를 저장할 변수
max_width = 0  # 가장 긴 가로길이를 저장할 변수
max_width_index = 0  # 가장 긴 가로길이의 인덱스를 저장할 변수
max_height_index = 0  # 가장 긴 높이의 인덱스를 저장할 변수
info = []  # 변의 정보들을 저장할 리스트
for i in range(6):
    temp = list(map(int, input().split()))
    info.append(temp)
    if temp[0] == 1 or temp[0] == 2:  # 만약 가로 길이라면
        if max_width < temp[1]:  # 해당 길이가 가장 길다면
            max_width = temp[1]  # 그 길이를 가장긴 가로로 저장한 후
            max_width_index = i  # 그에 해당하는 인덱스를 저장
    else:
        if max_height < temp[1]:  # 해당 길이가 가장 길다면
            max_height = temp[1]  # 그 길이를 가장긴 세로로 저장한 후
            max_height_index = i  # 그에 해당하는 인덱스를 저장

# 그 후 가장 긴 가로 및 세로와 인접한 변 2개와 가장긴 가로와 세로 총 4개를 새로운 리스트에 저장한다.
index_list = [info[max_height_index - 1], info[(max_height_index + 1) % 6], info[max_width_index - 1],
              info[(max_width_index + 1) % 6]]

product = 1  # 곱을 저장할 변수
for i in info:  # 입력받은 변들 중에
    if i not in index_list:  # 만약 새로운 리스트에 저장한 변 4개 중에 없다면 빈 사각형이므로
        product *= i[1]  # 그 넓이를 변수에 저장한다.

result = (max_width * max_height - product) * K  # 전체 큰 직사각형 넓이에서 빈 사각형 넓이를 빼준 후 K를 곱한다.
print(result)