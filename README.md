# Programa de Codificación y Decodificación de Cadenas en Python 🔠🔢

## Descripción 📄

Este programa en Python permite codificar una cadena de texto ingresada por teclado utilizando un método específico de normalización y conversión basado en una tabla de coordenadas. El programa también permite realizar el proceso inverso, es decir, decodificar una cadena previamente codificada para obtener el texto original.

## Tabla de Coordenadas 📊

Utilizamos la siguiente tabla para la conversión de letras a pares de números:
```

   0   1   2   3   4
9 | A | B | C | D | E
8 | F | G | H | I | J
7 | K | L | M | N | O
6 | P | Q | R | S | T
5 | U | V | W | X | Y | Z

```
## Ejemplo de Codificación

```python
print(codifica('hola mundo'))  # Resultado esperado: '827370907164729373'
