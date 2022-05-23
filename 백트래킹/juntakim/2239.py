sdoku = []
for i in range(9):
    sdoku.append(list(map(int, input())))

blank = []
count = 0
for i in range(9):
    for j in range(9):
        if sdoku[i][j] == 0:
            blank.append([i, j])
            count += 1

def checkrowandcolandbox(num, x, y):
    for i in range(9):
        if sdoku[x][i] == num:
            return False
        if sdoku[i][y] == num:
            return False
    a = x // 3 * 3
    b = y // 3 * 3
    for i in range(a, a + 3):
        for j in range(b, b + 3):
            if sdoku[i][j] == num:
                return False
    return True

def dfs(index):
    if index == count:
        for i in range(9):
            for j in range(9):
                print(sdoku[i][j], end='')
            print()
        exit(0)
    x, y = blank[index]
    for i in range(1, 10):
        if checkrowandcolandbox(i, x, y):
            sdoku[x][y] = i
            dfs(index + 1)
            sdoku[x][y] = 0
dfs(0)