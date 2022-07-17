def stars(n):
  if n==1:
    return ['*']
  Stars=stars(n//3)
  L=[]
  for star in Stars:
    L.append(star*3)
  for star in Stars:
    L.append(star+' '*(n//3)+star)
  for star in Stars:
    L.append(star*3)
  return L

N=int(input())
print('\n'.join(stars(N)))
