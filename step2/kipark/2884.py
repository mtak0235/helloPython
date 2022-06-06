H, M = map(int, input().split())

if M < 45:
    if H == 0:
        H = 23
    else:
        H = H - 1
    print(H,60-(45-M))
else:
    print(H,M - 45) 