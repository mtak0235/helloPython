'''
파이썬으로 C 느낌으로 코딩 
st = input()

l = len(st)
w_cnt = 0

for i in range(l):
    w_cnt += 1
    if st[i] == '=':
        if i - 1 >= 0 and (st[i - 1] == 'c' or st[i - 1] =='s' or st[i - 1] =='z'):
            if i - 2 > 0 and st[i - 1] == 'z' and st[i - 2] == 'd':
                w_cnt -= 2
            else:
                w_cnt -= 1
    elif st[i] == '-':
        if i - 1 >= 0 and (st[i - 1] == 'd' or st[i - 1] =='c'):
            w_cnt -= 1
    elif st[i] == 'j':
        if i - 1 >= 0 and (st[i - 1] == 'l' or st[i - 1] == 'n'):
            w_cnt -= 1

print(w_cnt) '''

# 파이썬식 날먹 코딩
st = input()
krp_wd = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
for i in range(8):
    st = st.replace(krp_wd[i], '!')
print(len(st))