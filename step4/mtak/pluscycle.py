import sys

cycle = 0
result = int(sys.stdin.readline())
lot = result
while True:
     lot = int(str(lot%10) + str((lot//10 + lot%10)%10))
     cycle += 1
     if result != lot : continue
     break
print(cycle)
     