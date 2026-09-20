a = list(map(int, input().split()))
unique = True
for i in range(len(a) - 1):
    if a[i] == a[i+1]:
        unique = False
if unique:
    print("list contains all unique elements!")
else:
    print("list does not  contains uniques elements")
