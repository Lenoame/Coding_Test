p = []
w, h = map(int, input().split())
n = int(input())

for i in range(w):
  p.append([])
  for j in range(h):
    p[i].append(0)

for i in range(n):
  l, d, x, y = map(int, input().split())
  x -= 1
  y -= 1
  for j in range(l):
    if d == 0:
      p[x][y+j] = 1
    else:
      p[x+j][y] = 1
  

for i in range(w):
  for j in range(h):
    print(p[i][j], end=' ')
  print()
