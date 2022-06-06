t = int(input())

### 거리 직접 구해서 푸는 방법
for _ in range(t):
    x, y = map(int, input().split())
    l = y - x
    cnt = 0
    tmp = 0
    while True:
        cnt+=1
        h = (cnt // 2)
        if cnt % 2 == 1:
            tmp = (h*(h+1)//2) + ((h+1)*(h+2)//2)
        else:
            tmp = (h*(h+1)//2) * 2
        if tmp >= l:
            print(cnt)
            break

'''
### 규칙 구해서 푸는 방법
원리는 직접 이동 횟수와 거리를 쓰다보면 규칙이 발견된다는 것
대충 1, 1, 2, 2, 3, 3, 4, 4, 5, 5 이런 식으로 거리 마다 이동 횟수가 1씩 증가한다는 뜻

t = int(input())

for _ in range(t):
    x, y = map(int, input().split())
    l = y - x
    cnt = 0
    mv = 1
    dist = 0
    while dist < l:
        cnt += 1
        dist += mv
        if cnt % 2 == 0:
            mv += 1
    print(cnt)
'''