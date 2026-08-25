def lists(s):
    largest = s[0]
    for i in s:
        if i > largest:
           largest = i
    return largest
            
s = list(map(int, input().split()))
print(lists(s))
  
