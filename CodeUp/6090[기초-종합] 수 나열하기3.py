a, b, c, d = map(int, input().split())
e = (a * b + c)

for i in range(1, d + 1):
    if i < (d - 1):
        e = (e * b + c)
    else:
        if d == 1:
            print(1)
        else:
            print(e)
            break
