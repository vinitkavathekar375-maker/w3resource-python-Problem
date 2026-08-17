def character(str):
    if len(str)>=3:
        if str.endswith("ing"):
            return (str+"ly")
        else:
            return (str)
    else:
        return ("")

print(character(input()))
