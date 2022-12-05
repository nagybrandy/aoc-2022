import string

abc = string.ascii_lowercase + string.ascii_uppercase

input = open('input.txt', 'r').read().split('\n')
chars = []
sum = 0
"""for e in input:
  f, s  = e[:int(len(e)/2)], e[int(len(e)/2):]
  flag = False
  i = 0
  while flag == False and i < len(f):
    if f[i] in s:
      sum += abc.index(f[i])+1
      flag = True 
    i+=1
print(sum)"""

for i in range(0,len(input), 3):
  flag = False 
  j = 0
  while flag == False and len(input[i]) > j:
    c = input[i][j]
    if c in input[i] and c in input[i+1] and c in input[i+2]:
      print(c)
      flag = True
      sum += abc.index(c)+1
    j+=1
print(sum)