#[9498]조건문, 시험성적
score = int(input())
if 90 <= score <= 100 :
    print ("A")
if 80 <= score < 90 :
    print ("B")
if 70 <= score < 80 :
    print ("C")
if 60 <= score < 70 :
    print ("D")
if score < 60 :
    print ("F")