# 1 ---------------------------------------------
word = input()
time = 0

for i in word:
    if ord(i) >= 65 and ord(i) < 68:
        time += 3
    elif ord(i) >= 68 and ord(i) < 71:
        time += 4
    elif ord(i) >= 71 and ord(i) < 74:
        time += 5
    elif ord(i) >= 74 and ord(i) < 77:
        time += 6
    elif ord(i) >= 77 and ord(i) < 80:
        time += 7
    elif ord(i) >= 80 and ord(i) < 84:
        time += 8
    elif ord(i) >= 84 and ord(i) < 87:
        time += 9
    elif ord(i) >= 87 and ord(i) <= 90:
        time += 10

print(time)

# 2 ---------------------------------------------
# alpha_list = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
# word = input()

# time = 0
# for unit in alpha_list:
#     for i in unit:
#         for x in word:
#             if i == x:
#                 time += alpha_list.index(unit) + 3

# print(time)