a = list(map(int, input().split()))
b = []
for i in range(len(a) - 1):
    c = a[i+1] - a[i]
    b.append(c)
print(b)
