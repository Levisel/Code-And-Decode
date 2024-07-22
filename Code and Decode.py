
# Codificación y Decodificación de una cadena
# Francisco Velasco R.
# Ejercicio: Realizar un programa en Python para codificar una cadena de texto ingresada por teclado de acuerdo al método descrito

# variables
fila = 0
columna = 0
cont = ""

# 1. Normalizar cadena (Al final)

# 2. Convertir cada letra del texto original a la pareja que corresponda la coordenada
# Obervación: Las letras "J" e "I", se encontraban juntas en la tabla original, por lo que se puso de forma manual a la letra "J" una
# posición de (4,0).
matriz = [['A', 'B', 'C', 'D', 'E'], ['F', 'G', 'H', 'I', 'K'], ['L', 'M', 'N', 'O', 'P'], ['Q', 'R', 'S', 'T', 'U'],
          ['V', 'W', 'X', 'Y', 'Z']]


# Función 1: Recibe como parámetro un carácter y con ayuda de las posiciones, se obtiene sus coordenadas en base a la matriz proporcionada
# EJ. codificarLetra('A') --> retorna = (90)
def codificarLetra(letra):
    final = None
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            if matriz[i][j] == letra:
                columna = j
                fila = 9 - i
            elif letra == 'J':  # Si la letra es "J", sus coordenadas son automaticamente designadas
                columna = 0
                fila = 4
    if columna is not None and fila is not None:
        final = str(fila) + str(columna)
    return final


# Función 2: Recibe como parametro la cadena que fue pedida al usuario anteriormente, y genera la codificación con ayuda del anterior método
# EJ. codificarCadena('hola superman') --> (827370906264749461719072)
def codificarCadena(cadena):
    codigo = ""
    for i in range(len(cadena)):
        letra = cadena[i]
        codigo += codificarLetra(letra)
    return codigo


# 3. Concatenar todas las parejas para formar la cadena codificada

# Función 3: Recibe como parámetro un par de numeros de la cadena codificada, y al encontrarse retorna la letra correspondiente
# EJ. decodificarNum('90') --> (A)
def decodificarNum(
        parNum):  # parNum => hace referencia al par de numeros en forma String para facilitar la comparacion con las pos. de la matriz
    letra = None
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            tempFila = str(i)
            tempColumna = str(j)
            pos = tempFila + tempColumna
            if pos == parNum:
                letra = matriz[i][j]
                break
    return letra


# Función 4: Recibe como parámetro el codigo que se desea decodificar, y genera finalmente la cadena en base a las coordenadas ingresadas
# EJ. decodificarCadena('919063719072536173918372') => (BATMANYROBIN)
def decodificarCadena(codigo):
    palabra = ""
    for i in range(0, len(codigo), 2):  # Al extraer dos numeros del codigo, se recorre de dos en dos
        temp = codigo[i:i + 2]
        fila = 9 - int(temp[0])
        columna = int(temp[1])
        parNum = str(fila) + str(columna)
        if parNum == '50':
            palabra += 'J'
        else:
            palabra += decodificarNum(parNum)
    return palabra

#-----------------------------------------------------------------------------------------------------------------------
# 1. Normalizar la cadena y Programa Finalizado
while (cont != 'n'):
    cont = 's'
    while (cont != 'n'):
        print("Bienvenido al programa \nPor favor, sigue las instrucciones:")
        print("Seleccione una opción \n1.Codificar cadena \n2.Decodificar cadena")
        opt = input("\nOpcion(1/2): ")
        if opt == '1':
            cadena = input("\nIngrese una cadena a codificar: ").upper().replace(" ", "")
            print(f"La cadena codificada es: '{codificarCadena(cadena)}'")
        elif opt == '2':
            codigo = input("Ingrese el codigo a decodificar: ")
            print(f"El codigo decodificado es: '{decodificarCadena(codigo)}'")
        cont = input("\n¿Desea continuar (S/N)? = ").lower()
        cls = lambda: print('\n' * 100)
        cls()







