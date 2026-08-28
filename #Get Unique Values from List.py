original = list(map(int, input().split()))
unique = list(map(int, input().split()))
for i in original:
    if i in unique:
        print(i,end=" ")
