def character(str, n):
    a = str[:n]
    b = str[n+1:]
    c = a + b
    return c
print(character(input(),int(input())))
