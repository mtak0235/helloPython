#
#
#

import sys


def find_root(n, P):
	if P[n] == n:
		return n
	return find_root(P[n], P)


def find_and_update_root(n, P):
	if P[n] == n:
		return n
	P[n] = find_and_update_root(P[n], P)
	return P[n]


if __name__ == "__main__":
	N = int(input().split()[0])
	P = [i for i in range(N + 1)]
	cmd_lines= [map(int, line.strip().split()) for line in sys.stdin.readlines()]

	results = []
	for cmd, a, b in cmd_lines:
		if cmd == 0:
			root_a = find_and_update_root(a, P)
			root_b = find_and_update_root(b, P)
			P[root_b] = root_a
		else:
			results.append(int(find_root(a, P) == find_root(b, P)))

	ret_str = ("NO", "YES")
	for result in results:
		print(ret_str[result])
