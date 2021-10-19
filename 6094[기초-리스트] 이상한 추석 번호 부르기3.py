a = int(input())
n = list(map(int, input().split()))
k = a
for i in n:
  if i <= k:
    k = i
  
print(k)
