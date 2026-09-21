a = list(map(int, input().split()))

for i in range(len(a)):
    if a[i]%2 != 0 and a[i] != 0 and a[i] != 1:
        print(a[i], "=" "Prime no")
    else:
        print(a[i], "=" "not prime no")
