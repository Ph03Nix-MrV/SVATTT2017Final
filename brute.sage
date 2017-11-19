f=open('solveme.txt').read()
ch = []
arr = f.split('\n\n')[:-1]
for line in arr:
  F(x,y) = line.split(' == ')[0]
  X = Integer(line.split(' == ')[1])
  c=False
  for i in range(512):
    for j in range(512):
      a = i+ 0x636f
      b = j+ 0x636f
      S = F(a,b)
      if Integer(S) ==Integer(X):
        ch.append(i)
        ch.append(j)
        c=True
        break
    if c:
      print ch
      break
