def column_number_to_title(column_number):
    result = ""
    while column_number > 0:
        # Calcula el residuo
        remainder = (column_number - 1) % 26
        # Convierte el residuo en letra
        result = chr(65 + remainder) + result
        # Actualiza el número dividiéndolo por 26
        column_number = (column_number - 1) // 26
    return result

# Ejemplos de uso
column_1 = column_number_to_title(1)
column_27 = column_number_to_title(27)

print("Columna 1:", column_1)  # Debe imprimir "A"
print("Columna 27:", column_27)  # Debe imprimir "AA"
