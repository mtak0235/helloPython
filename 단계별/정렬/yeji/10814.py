#[10814]정렬, 나이순 정렬
#나이가 증가하는 순, 나이가 같으면 먼저 가입한 사람이 앞에 오는 순서
import sys
n = int(sys.stdin.readline())
member = []
for i in range(n):
    member.append(list(sys.stdin.readline().split()))
member.sort(key=lambda x: int(x[0]))
for i in range(n):
    print(member[i][0], member[i][1])