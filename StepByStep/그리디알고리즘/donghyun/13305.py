import sys

input = sys.stdin.readline
n = int(input())
roads = list(map(int, input().split()))
cities = list(map(int, input().split()))
cities.pop()
m = cities[0]
cost = 0
for road, city in zip(roads, cities):
	m = min(m, city)
	cost += road * m
print(cost)