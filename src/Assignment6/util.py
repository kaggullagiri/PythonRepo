def print_formatted(number):
    width = len(bin(number)[2:])
    for i in range(1, number + 1):
        deci, octa, hexa, bina = str(i), oct(i)[2:], hex(i)[2:].upper(), bin(i)[2:]
        print(deci.rjust(width), octa.rjust(width), hexa.rjust(width), bina.rjust(width))
