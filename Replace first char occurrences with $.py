def character(str):
    a=(str.lower())
    b=(a.replace(a[0],"$"))
    return (a[0]+b.lstrip("$"))

print(character(input()))
