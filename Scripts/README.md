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

### Bubble Sort

El método Bubble Sort, o Ordenamiento Burbuja, es un algoritmo de ordenación simple y fácil de entender. Opera comparando pares de elementos adyacentes en una lista y realizando intercambios si están en el orden incorrecto. Este proceso se repite hasta que la lista esté completamente ordenada.

#### Funcionamiento:

1. Comienza comparando el primer elemento con el segundo.
2. Si el primer elemento es mayor que el segundo, se intercambian.
3. Luego, compara el segundo con el tercero, y así sucesivamente, hasta llegar al final de la lista.
4. Después de la primera pasada, el elemento más grande estará en la última posición.
5. Repite este proceso para todos los elementos restantes, ignorando el último elemento en cada pasada ya que ya está en su posición correcta.
6. Continúa estas iteraciones hasta que no se realicen más intercambios, lo que indica que la lista está ordenada.

#### Conveniencia de uso:

El Bubble Sort es adecuado para pequeñas listas o en casos donde la simplicidad y la comprensión del algoritmo son prioritarias sobre la eficiencia. Sin embargo, en términos de eficiencia, su desempeño es pobre para listas grandes, ya que su complejidad es de O(n^2), lo que significa que el tiempo de ejecución aumenta cuadráticamente con el tamaño de la lista.

#### Ejemplo conceptual:

Tomemos la lista [34, 7, 23, 32, 5] como ejemplo:

1. Comenzamos comparando 34 y 7. Como 34 es mayor que 7, los intercambiamos: [7, 34, 23, 32, 5].
2. Luego, comparamos 34 y 23. No hay necesidad de intercambiar: [7, 23, 34, 32, 5].
3. Continuamos con 34 y 32. Se intercambian: [7, 23, 32, 34, 5].
4. Ahora, comparamos 34 y 5. Se intercambian: [7, 23, 32, 5, 34].
5. En la primera pasada, el elemento más grande (34) se coloca en su posición final. Repetimos el proceso con los elementos restantes.
6. Después de algunas iteraciones adicionales, obtenemos la lista ordenada: [5, 7, 23, 32, 34].

Aunque el Bubble Sort es fácil de entender y aplicar, su uso se limita principalmente a fines educativos o para ordenar conjuntos de datos muy pequeños debido a su baja eficiencia en términos de tiempo de ejecución.

## Ejercicio Functools

### Descripción
Este proyecto implementa una clase `SimpleOperations` en Python, que proporciona métodos para calcular descuentos y tasas de impuestos. Utiliza la herramienta `functools.partial` para crear versiones especializadas de estas funciones con parámetros predefinidos.

### Funcionalidades
- `apply_discount(price, discount)`: Aplica un descuento al precio dado y retorna el nuevo precio.
- `calculate_tax(price, tax_rate)`: Calcula y agrega el impuesto al precio dado.

### Uso
1. Clona este repositorio en tu máquina local.
2. Asegúrate de tener Python instalado en tu sistema.
3. Ejecuta el archivo `SimpleOperations.py`.

## Link al repositorio de GitHub
https://github.com/AlvaroSantamariaAnton/ALGORITMOS_2_Alvaro_Santamaria_Anton.git