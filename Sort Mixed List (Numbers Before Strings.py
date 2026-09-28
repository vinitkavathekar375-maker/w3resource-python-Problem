a = input().split()
b = []
c = []
for i in range(len(a)):
    if a[i].isdigit():
        b.append(a[i])
    else:
        c.append(a[i])
print(b)
print(c)
        
