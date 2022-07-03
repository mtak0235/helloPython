word = input()

letters = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
for i in letters :
	word = word.replace(i, 'a')
print(len(word))
