def StringMutation(string, position, character):
    num = list(string)
    num[position] = character
    string = "".join(num)
    return string
    

