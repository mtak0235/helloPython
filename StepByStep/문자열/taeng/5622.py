# boj 5622
# 다이얼

import sys

lookup = {}
lookup["A"] = 2
lookup["B"] = 2
lookup["C"] = 2
lookup["D"] = 3
lookup["E"] = 3
lookup["F"] = 3
lookup["G"] = 4
lookup["H"] = 4
lookup["I"] = 4
lookup["J"] = 5
lookup["K"] = 5
lookup["L"] = 5
lookup["M"] = 6
lookup["N"] = 6
lookup["O"] = 6
lookup["P"] = 7
lookup["Q"] = 7
lookup["R"] = 7
lookup["S"] = 7
lookup["T"] = 8
lookup["U"] = 8
lookup["V"] = 8
lookup["W"] = 9
lookup["X"] = 9
lookup["Y"] = 9
lookup["Z"] = 9

alpha = sys.stdin.readline().rstrip()

tot = 0
for c in alpha:
    tot += lookup[c]
tot += len(alpha)
print(tot)