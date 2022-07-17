#
#
#

import itertools

if __name__ == "__main__":
    N, M = map(int, input().split())
    _cards = tuple(map(int, input().split()))
    cards = tuple([card for card in _cards if card <= M])
    print(max([sum(arr) for arr in set(itertools.combinations(cards, 3)) if sum(arr) <= M]))
