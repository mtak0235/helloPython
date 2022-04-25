while True:
    word = input()
    palindrom = word[::-1]
    if word=='0':
        break
    if word==palindrom:
        print('yes')
    else:
        print('no')
