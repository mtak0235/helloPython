#
#
#

import sys


class Trie:
    def __init__(self):
        self.point = 0
        self.next = {}

    def push(self, _word: str):
        cur: Trie = self
        for _ch in _word:
            if _ch not in cur.next:
                cur.next[_ch] = Trie()
            cur = cur.next[_ch]
            cur.point += 1

    def count(self, _word: str) -> int:
        cur: Trie = self
        cnt: int = 0
        pre_point: int = 0
        for _ch in _word:
            cur = cur.next[_ch]
            if cur.point != pre_point:
                cnt += 1
                pre_point = cur.point
        return cnt


if __name__ == "__main__":
    raw = sys.stdin.readlines()
    ROOT, words = Trie(), []
    N = -1
    ret = []
    for line in raw:
        if (line.strip()).isnumeric():
            if N != -1:
                push_cnt = 0
                for word in words:
                    push_cnt += ROOT.count(word)
                ret.append(f"{round(push_cnt / len(words), 2):.2f}")
            ROOT, words = Trie(), []
            N = int(line.strip())
            continue
        word = line.strip()
        words.append(word)
        ROOT.push(word)
    else:
        push_cnt = 0
        for word in words:
            push_cnt += ROOT.count(word)
        ret.append(f"{round(push_cnt / len(words), 2):.2f}")
    print("\n".join(ret))

