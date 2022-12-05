file = open('input.txt', 'r').read().split('\n')

s = []
cols = 0
moves = [ ]
for a in file:
  if '[' in a:
    s.append(a)
  elif 'move' in a:
    new = []
    a.split(" ")
    n = a.split(' ')
    new.append(int(n[1]))
    new.append(int(n[3])-1)
    new.append(int(n[5])-1)
    moves.append(new)
print(moves)

st = []
for e in s:
  new = []
  for i in range(1, len(e), 4):
    new.append(e[i])
    print(e[i])
  st.append(new)
st = st[::-1]

a = []
for i in range(len(st[0])):
  new = []
  for e in st:
    if e[i] != ' ':
      new.append(e[i])
  a.append(new)

print(a)
for m in moves:
  new = []
  for i in range(m[0]):
    if a[m[1]] != []:
      new.append(a[m[1]].pop())
  for i in range(len(new)):
    a[m[2]].append(new.pop())

for l in a:
  if l != []:
    print(l.pop(), end='')