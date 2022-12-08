f = open('input.txt', 'r').read()

for i in range(len(f)):
  n = []
  for j in range(14):
    if f[i+j] not in n:
      n.append(f[i+j])
  if len(n) == 14: 
    print(i+14)
    exit()
    