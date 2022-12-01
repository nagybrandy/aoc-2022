#one-liner for the first part 

print(max(([sum(int(i) for i in j.split('\n')) for j in open('input.txt').read().split('\n\n')])))


# fastest
f = open('input.txt','r').read().split('\n')
s = 0
sums = []
for e in f:
  if e != '': 
    s += int(e)
  else:
    sums.append(s)
    s = 0
print(sum(sorted(sums, reverse=True)[0:3]))


