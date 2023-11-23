def listproblem(commands):
    El = []  # empty list

    for com in commands:
        if com[0] == "insert":
            El.insert(int(com[1]),int(com[2])) #
        elif com[0] == "print":
            print(El)
        elif com[0] == "remove":
            e = int(com[1])
            El.remove(e)
        elif com[0] == "append":
            e = int(com[1])
            El.append(e)
        elif com[0] == "sort":
            El.sort()
        elif com[0] == "pop":
            El.pop()
        elif com[0] == "reverse":
            El = El[::-1]

    return El  # Return the modified list
