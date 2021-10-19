a, b, c = map(int, input().split())
i = 0; j = 0; k = 0;
for i in range(a):
    for j in range(b):
        for k in range(c):
            print(i, j, k)
            
print(a*b*c)
