import itertools

N, M = map(int, input().split())
card = list(map(int, input().split()))

comb = [sum(comb) for comb in itertools.combinations(card, 3) if sum(comb) <= M]

print(max(comb))
