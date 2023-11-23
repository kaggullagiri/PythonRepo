def printingpattern(thickness, c='H'):
    result = []

    # Top Cone
    for i in range(thickness):
        line = (c * i).rjust(thickness - 1) + c + (c * i).ljust(thickness - 1)
        result.append(line)

    # Top Pillars
    for i in range(thickness + 1):
        line = (c * thickness).center(thickness * 2) + (c * thickness).center(thickness * 6)
        result.append(line)

    # Middle Belt
    for i in range((thickness + 1) // 2):
        line = (c * thickness * 5).center(thickness * 6)
        result.append(line)

    # Bottom Pillars
    for i in range(thickness + 1):
        line = (c * thickness).center(thickness * 2) + (c * thickness).center(thickness * 6)
        result.append(line)

    # Bottom Cone
    for i in range(thickness):
        line = ((c * (thickness - i - 1)).rjust(thickness) + c + (c * (thickness - i - 1)).ljust(thickness)).rjust(thickness * 6)
        result.append(line)

    return result