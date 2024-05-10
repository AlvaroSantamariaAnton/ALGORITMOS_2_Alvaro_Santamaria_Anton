# Álvaro Santamaría Antón

## EJERCICIO POO

Este repositorio contiene dos scripts de Python para gestionar un catálogo de música. 
El primero define un enum de géneros musicales, mientras que el segundo define una clase para representar canciones.

### Scripts

#### genre.py

Este script define un enum llamado `GENRE` que representa diferentes géneros musicales.

Enum `GENRE`:

- `ROCK`: Representa el género musical rock.
- `POP`: Representa el género musical pop.
- `EDM`: Representa el género musical EDM (Electronic Dance Music).
- `COUNTRY`: Representa el género musical country.

#### song.py

Este script define la clase `Song`, que representa una canción con sus atributos y métodos asociados.

Clase `Song`:

La clase `Song` representa una canción y tiene los siguientes atributos:

- `id`: Identificador único de la canción.
- `name`: Nombre de la canción.
- `artist`: Nombre del artista que interpreta la canción.
- `duration`: Duración de la canción en segundos.
- `release_date`: Fecha de lanzamiento de la canción.
- `genres`: Lista de géneros de la canción.

La clase `Song` proporciona los siguientes métodos:

- `__init__(id, name, artist, duration, release_date, genres=[])`: Constructor de la clase para inicializar una canción con los atributos proporcionados.
- `get_id()`: Método para obtener el identificador único de la canción.
- `get_name()`: Método para obtener el nombre de la canción.
- `get_artist()`: Método para obtener el nombre del artista de la canción.
- `get_duration()`: Método para obtener la duración de la canción en segundos.
- `get_release_date()`: Método para obtener la fecha de lanzamiento de la canción.
- `get_genres()`: Método para obtener la lista de géneros de la canción.
- `add_genre(genre)`: Método para añadir un género a la lista de géneros de la canción.
- `__eq__(other)`: Método para comparar dos canciones basadas en su identificador único.
- `__str__()`: Método para representar la canción como una cadena legible.

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

## Ejercicio de Ordenación



## Link al repositorio de GitHub
https://github.com/AlvaroSantamariaAnton/ALGORITMOS_2_Alvaro_Santamaria_Anton.git