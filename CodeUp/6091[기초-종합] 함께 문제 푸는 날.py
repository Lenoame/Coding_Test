a, b, c = map(int, input().split())
d = 1
while True:
    if d % a != 0 or d % b != 0 or d % c != 0:
        d += 1
    else:
        print(d)
        break
