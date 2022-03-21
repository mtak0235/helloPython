from ast import While


while True:
        try:
            A, B = map(int,  input().split())
            print(A+B)
        except:
            break