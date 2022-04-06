#[15652]백트래킹, N과 M(4)
'''
1부터 N까지 자연수 중에서 M개를 고른 수열
같은 수를 여러 번 골라도 된다.
고른 수열은 비내림차순이어야 한다.
길이가 K인 수열 A가 A1 ≤ A2 ≤ ... ≤ AK-1 ≤ AK를 만족하면
즉 순열의 오른쪽 요소가 크거나 같으면 비내림차순이라고 한다.
'''

n,m = map(int, input().split())
 
s = []
 
def dfs(start):
    if len(s)==m:
        print(' '.join(map(str,s)))
        return
    #1부터 n까지 모든 숫자를 사용했지만 [2,1]과 같이 앞의숫자가 뒤의숫자보다 작은경우를 제외하기위해 start부터 n까지 숫자를 사용
    #리스트에 들어간 수열들이 m개가 되면 리스트에 들어있는 숫자들을 모두 출력
    
    for i in range(start, n+1): # for문을 이용하여 start부터 n까지의 숫자들을 모두 확인
        s.append(i)
        dfs(i)
        s.pop()
    
dfs(1)