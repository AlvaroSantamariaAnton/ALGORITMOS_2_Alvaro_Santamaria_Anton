# Álvaro Santamaría Antón

## EJERCICIO POO


## Ejercicio de Recursividad: Cálculo del Factorial

### Especificación

Nombre de la Función:
`factorial`

Descripción:
Esta función calcula el factorial de un número entero no negativo utilizando recursión.

Parámetros de Entrada:
- `n` : int - Número entero al que se le calculará el factorial.

Salida:
- `result` : int - El factorial del número dado.

Algoritmo:
La función `factorial` se implementa utilizando recursión. Calcula el factorial del número dado siguiendo los siguientes pasos:
1. **Caso Base:** Si `n` es 0, retorna 1.
2. **Paso Recursivo:** Si `n` es mayor que 0, retorna `n * factorial(n-1)`.

### Pseudocódigo

```python
"""
Función factorial(n):
    Si n es igual a 0:
        Retorna 1
    Sino:
        Retorna n multiplicado por factorial(n-1)
"""
```

### Comportamiento y Restricciones

Precondición:
- El parámetro `n` debe ser un número entero no negativo.

Poscondición:
- La función retorna el factorial del número `n`.

Datos de Entrada:
- `n` debe ser un número entero no negativo.

Datos de Salida:
- El resultado es un número entero, el factorial de `n`.

Hipótesis:
- Se espera que el script funcione correctamente para valores de `n` dentro del rango soportado por la representación de enteros en Python.

Efecto:
- La función debe ser eficiente y retornar el resultado correctamente incluso para valores grandes de `n`.
