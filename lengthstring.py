string = "holaquetalestastodobienoque"

def longitud(string):
    cont = 0
    for a in range(len(string)):
        cont += 1
    return cont

longitud(string)
print(string, "tiene", longitud(string), "caracteres")
