a, b, c = map(int, input().split())
e = a*b*c
f = e / 8 / 1024 / 1024
print(format(f, ".2f"),'MB')
