import sys, string

H, M = map(int, sys.stdin.readline().split())

# if 정석
def printFastenAlarm(H, M):
    M -= 45
    if M < 0:
        M += 60
        H -= 1
    if H < 0:
        H = 23
    print("%d %d" %(H,M))
printFastenAlarm(H,M)