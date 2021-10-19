a, b, c, d = map(int, input().split())
e = a*b*c*d
f = e / 8 / 1024 / 1024
print(format(f, ".1f"),'MB')
