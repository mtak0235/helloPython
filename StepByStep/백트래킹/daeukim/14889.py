# 스타트와 링크
from itertools import combinations
import sys
input = sys.stdin.readline

n = int(input()) # n명(짝수)
s_list = [list(map(int, input().split())) for _ in range(n)] # 능력치 배열
s = [i for i in range(n)] # 팀 조합을 위한 배열
teams = []
for team in list(combinations(s, n//2)):
  teams.append(team)

min_dif = 1e9
for i in range(len(teams)//2):
  start = 0
  link = 0
  for j1 in range(n//2 - 1):
    for j2 in range(j1+1, n//2):
      start += s_list[teams[i][j1]][teams[i][j2]]
      start += s_list[teams[i][j2]][teams[i][j1]]
      link += s_list[teams[-1-i][j1]][teams[-1-i][j2]]
      link += s_list[teams[-1-i][j2]][teams[-1-i][j1]]
  min_dif = min(min_dif, abs(start - link))
print(min_dif)