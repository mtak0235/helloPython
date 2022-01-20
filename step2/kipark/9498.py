grade = ['A', 'B', 'C', 'D']
grade_cut = [90, 80, 70, 60]
student = int(input())
for i in range(0, len(grade)):
    if student >= grade_cut[i]:
        print(grade[i])
        break
if student < 60:
    print("F")