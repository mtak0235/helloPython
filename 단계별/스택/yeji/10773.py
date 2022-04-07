#[10773]step18,제로
import sys
k = int(sys.stdin.readline()) #여기에 int(input())이 와도 된다. 

stack=[]

for i in range(k):
    command = int(input())

    if command == 0:
        stack.pop()
    else:
        stack.append(command)

print(sum(stack))