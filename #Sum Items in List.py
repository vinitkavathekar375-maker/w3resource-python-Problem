def lists(s):
    total = 0
    for i in s:
        total = total + i
    return total
s = list(map(int, input().split()))

print(lists(s))
    
