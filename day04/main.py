file = [i.split(',') for i in open('input.txt', 'r').read().split('\n')]

sum = 0
for e in file:
  f, s = [int(i) for i in e[0].split('-')],  [int(i) for i in e[1].split('-')]
  if (f[0] <= s[1] and s[1] <= f[1]) or (s[0] <= f[1] and f[1] <= s[1]):
    sum+=1

print(sum)