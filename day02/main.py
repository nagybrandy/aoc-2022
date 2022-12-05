a = 'ABC'
x = 'XYZ'

f = [i.split(" ") for i in open('input.txt', 'r').read().split('\n')]

points = 0

for k in f:
  e = k[0]
  m = k[1]
  points += x.index(m)+1
  if a.index(e) == x.index(m):
    points += 3
  elif e == a[x.index(m)-1]:
    points += 6

#part2
points2 = 0
for k in f:
  e = k[0]
  m = k[1]
  if m == 'X':
    v = a.index(e)-1
    points2 += v+1
  elif m == 'Y':
    points2 += a.index(e)+1+3
  elif m == 'Z':
    points2 += a.index(a[a.index(e)-1])+6
  print(e,m,points2)
print(points2)