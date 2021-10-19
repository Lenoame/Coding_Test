a = int(input(), 16)
n = 0
while n < 15:
    n += 1
    print('%X'%a, '*%X'%n, '=%X'%(a * n), sep='')
