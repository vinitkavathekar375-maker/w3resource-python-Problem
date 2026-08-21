def character(s):
    result = ""

    for i in s:
        if i not in result:
            result += i

    return result

print(character(input()))
