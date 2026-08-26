def lists(s):
    count = []
    for i in s:
        if i not in count:
            count.append(i)
    return count
          
s = list(map(int, input().split()))

print(lists(s))
        
