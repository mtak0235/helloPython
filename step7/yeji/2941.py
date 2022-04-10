#[2941]step7,크로아티아 알파벳

croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z='] #크로아티아 알파벳
word = input() #문자 입력받기

for i in croatia :
    word = word.replace(i, '+')  # 입력받은 문자에서 크로아티아 알파벳을 한 문자(+)로 변환(replace)
print(len(word)) #변환된 문자열의 총 글자 수 