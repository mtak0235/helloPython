#8958 ox퀴즈
#문제를 맞은 경우 그 문제의 점수는 그 문제까지 연속된 O의 개수

n = int(input()) #테스트 케이스의 개수

for i in range(n): 
    ox = input() #ox입력
    s = list(ox)
    sum = 0
    c = 1
    
    for i in s:
        if i == 'O':
            sum += c
            c += 1
        else:
            c = 1
    
    print(sum)