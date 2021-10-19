a = int(input())
n = 0
i = 0
while n < a:
    i += 1
    n += i
    if n > a:
        break
    
print(n)
