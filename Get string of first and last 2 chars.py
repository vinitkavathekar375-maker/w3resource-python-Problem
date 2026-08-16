def character(str):
    if len(str)<2:
        return("empty string")
    else:
        return(str[0]+str[1]+str[-1]+str[-2])
        
print(character('w3resource'))
