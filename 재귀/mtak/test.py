import sys

def move(num2Move, _from, _to, _spare):#3, 1, 3, 2
	print(_from, _to)
	move1(num2Move - 1, _from, _spare, _to)

def move1(num2Move, _from, _to, _spare):#2, 1, 2, 3
	print(_from, _to)
	move2(num2Move - 1, _spare, _to, _from)

def move2(num2Move, _from, _to, _spare):#1, 3, 2, 1 
	print(_from, _to)
	move3(num2Move - 1, _spare, _from, _to)

def move3(num2Move, _from, _to, _spare):#0, 1, 3, 2
	print(_from, _to)
	move4()

_plateCnt = int(sys.stdin.readline()) //3
move(_plateCnt, 1, 3, 2)