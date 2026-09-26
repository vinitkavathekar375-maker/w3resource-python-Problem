n = int(input("Enter the no.list"))
a=[]
for i in range(n):
        x = list(map(int, input().split()))
        a.append(x)
b =[]
for i in range(len(a)):
    b.append(list(reversed(a[i])))
print(b)
