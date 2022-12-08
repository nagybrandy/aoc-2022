f = open('input.txt', 'r').read().split('\n')
path = []
folders = {}

for l in f:
  if '/' in l:
    path = ['/']
    folders['/'] = 0
  elif '..' in l:
    path.pop()
  elif 'cd ' in l:
    new = l[5:]
    path.append(new)
    lll = ''.join(path)
    folders[lll] = 0
  elif '$ ' not in l and 'dir' not in l:
    lstr = ''.join(path)
    folders[lstr] += int(l.split(' ')[0])
    pc = path.copy()
    for i in range(len(path)-1):
      pc.pop()
      lstr2 = ''.join(pc)
      folders[lstr2] += int(l.split(' ')[0])
sum = 0

vals = folders.values()
for e in vals:
  if e < 100000:
    sum += e
print('part1', sum)

for e in folders:
  print(e)
  
  
free = 70000000 - folders["/"]
needed = 30000000 - free
smallest = float('inf')
for e in vals:
  if e > needed and e < smallest:
    smallest = e
    print(smallest)

print('part2',smallest)