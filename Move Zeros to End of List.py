a = list(map(int, input().split()))
b= []
i=0
for i in a:
    if i != 0:
        b.append(i)
for i in a:
    if i == 0:
        b.append(i)
print(b)
