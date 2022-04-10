num_arr = list(map(int,input().split()))
result = []

while num_arr[0] != 0 and num_arr[1] != 0 and num_arr[2] != 0:
    num_arr.sort()
    if num_arr[0]**2 + num_arr[1]**2 == num_arr[2]**2:
        print("right")
    else:
        print("wrong")
    num_arr = list(map(int,input().split()))
