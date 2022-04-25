import sys
from itertools import combinations
input = sys.stdin.readline

n = int(input())
members = [i for i in range(n)]
matrix = []
for _ in range(n):
    matrix.append(list(map(int, input().split())))
minimum = sys.maxsize

for team1 in combinations(members, n // 2):
    team2 = list(set(members) - set(team1)) 
    sum1 = 0
    sum2 = 0
    for mem in combinations(team1, 2):
        sum1 += matrix[mem[0]][mem[1]]
        sum1 += matrix[mem[1]][mem[0]]
    for mem in combinations(team2, 2):
        sum2 += matrix[mem[0]][mem[1]]
        sum2 += matrix[mem[1]][mem[0]]
    minimum = min(minimum, abs(sum1 - sum2))

print(minimum)