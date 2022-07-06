# 가장 흔한 단어
def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
	words = [word for word in re.sub(r'[^\w]', ' ', paragraph).lower().split() if word not in banned]
	counts = collections.Counter(words)
	return conuts.most_common(1)[0][0]