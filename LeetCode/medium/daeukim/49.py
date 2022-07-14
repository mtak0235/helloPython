# 그룹 애너그램
import collections

strs = ["eat","tea","tan","ate","nat","bat"]

dic = collections.defaultdict(list)
answer = []
for ana in strs:
    k = ''.join(sorted(ana))
    dic[k].append(ana)
for value in dic.values():
    answer.append(value)
print(answer)