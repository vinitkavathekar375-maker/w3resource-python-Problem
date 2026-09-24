a = list(map(int, input().split()))
b = []
c = []
u = int(input())
for i in range(u,len(a)):
    b.append(a[i])

for i in range(0,u):
    c.append(a[i])

print(b + c)
