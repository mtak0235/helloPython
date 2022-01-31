t = int(input())
result = []

for _ in range(t):
    k = int(input())    # 층 수
    n = int(input())    # 호 수
    f0 = [i for i in range(1, n + 1)]   # 0층: 1호 ~ n호 사람 수
    for _ in range(k):  # 층 수만큼 반복
        for i in range(1, n):   # 1 ~ n-1까지 (인덱스로 사용)
            f0[i] += f0[i - 1]  # 층별 각 호실의 사람 수를 변경 
    result.append(f0[-1])   # 가장 마지막 수 출력

for i in range(t):
    print(result[i])