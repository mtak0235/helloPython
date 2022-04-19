#[1037]9370_수학, 약수
#어떤 수 N의 진짜약수(1,N제외)가 주어질 때,N구하기

nn =int(input()) #N의 진짜 약수의 개수
ny = list(map(int,input().split())) #N의 진짜 약수가 모두 주어짐

#약수가 모두 주어졌을때 가장 큰 수와 가장 작은 수를 곱하면 N의 값이다.
n_max = max(ny) #최대값
n_min = min(ny) #최소값

print(n_max * n_min) #최대값과 최소값의 곱 출력