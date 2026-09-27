a = list(map(int, input().split()))
b = []
for i in range(len(a)):
    b.append(a[i])
c = max(b)
d = min(b)

print("Max index no.= ", [i for i in range(len(a)) if b[i] == c])
print("Min index no.= ", [i for i in range(len(a)) if b[i] == d])

# OUTPUT
#  123 45 6 2 56  1 2312 9 1
# Max index no.=  [6]
# Min index no.=  [5, 8]
