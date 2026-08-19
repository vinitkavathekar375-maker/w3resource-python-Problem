def character(s):
    count = dict()
    words = s.split()
    for n in words:
        if n in count:
            count[n] += 1
        else:
            count[n] = 1
    return count

print(character(input()))
        
