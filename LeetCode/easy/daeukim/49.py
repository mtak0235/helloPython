# 그룹 애너그램

def groupAagrams(self, strs:List[str]) -> List[List[str]]:
	anagrams = collections.defaultdict(list)

	for word in strs:
		anagrams[''.join(sorted(word))].append(word)
	return list(anagrams.values())