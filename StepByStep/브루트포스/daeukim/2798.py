# 블랙잭
from itertools import combinations

n, m = map(int, input().split())
card = list(map(int, input().split()))
card_list = list(combinations(card, 3))
max_s = 0
for card in card_list:
	s = sum(card)
	if s <= m:
		max_s = max(max_s, s)
print(max_s)