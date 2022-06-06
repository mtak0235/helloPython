# 1 ---------------------------------------------
word = input()
count_list = [0 for _ in range(26)]

for i in word:
    count_list[ord(i.upper()) - 65] += 1

max_num = max(count_list)

if count_list.count(max_num) > 1:
    print('?')
else:
    print(chr(count_list.index(max_num) + 65))

# 2 ---------------------------------------------
# inputData = input().upper()
# searchKeys = list(set(inputData))

# countArr = []
# for key in searchKeys:
#     countArr.append(inputData.count(key))

# if countArr.count(max(countArr)) > 1:
#     print("?")
# else:
#     print(searchKeys[countArr.index(max(countArr))])