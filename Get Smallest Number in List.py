def lists(s):
    smallest = s[0]
    for i in s:
        if i < smallest:
            smallest = i
    return smallest
    
        
s = list(map(int, input().split()))
print(lists(s))
