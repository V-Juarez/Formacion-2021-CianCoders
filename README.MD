# Python
<p align="center"><a href=""><img src="https://www.python.org/static/community_logos/python-logo-master-v3-TM-flattened.png" width="600"></a></p>

# Tabla de contenido
- [¿Qué es la programación?](#¿Qué-es-la-programación?)
  - [¿Por qué programar con Python?](#¿Por-qué-programar-con-Python?)
  - [Operadores matemáticos](#Operadores-matemáticos)
  - [Variables y expresiones](#Variables-y-expresiones)
  - [Funciones](#Funciones)
  - [Estructuras condicionales](#Estructuras-condicionales)
- [Uso de strings y ciclos](#Uso-de-strings-y-ciclos)
  - [Strings en Pyhton](#Strings-en-Pyhton)
  - [Operaciones con strings](#Operaciones-con-strings)
- [](#)
- [](#)

# ¿Qué es la programación?
 
  * Ciencia de la computación 
    * Matemáticas
    * Ingeniería
    * Ciencia
  * La habilidad más importante: Resolver problemas
  * Un programa es una secuencia de intrucciones que describe cómo realizar un cómputo.
  * Casi todos los programas realizan las siguientes tareas:
    * Input
    * Output
    * Operaciones matemáticas
    * Ejecución condicional
    * Repeticiones
     
## ¿Por qué programar con Python?

  * Comunidad
  * Facultad de uso
  * librerías
  * Popularidad
  * Industria

## Operadores matemáticos

```python
+
-
/
//
%
*
**
```
 ## Variables y expresiones
  
  * ¿Qué es una variable?
  * Tipos de variables públicas, privadas, constantes.
  * Una asignación (assignment statement) crea una variable y le asigna un valor.
    * message = 'How are you?'
    * _age = 20
    * PI = 3.14159
    * __do not_touch = 'Something important'
  * Las variables se pueden reasignar
    * my_var = 2
    * my_var = my_var_*5
    * print(my_var)

  * Variables
   * Pueden contener númerosy letras
   * No debe comenzar con número
   * Múltiples palabras se unen con _
      * multiple_words
   * No se pueden utilizar [palabras reservadas](https://ellibrodepython.com/palabras-reservadas-python)

   * __[turtle](https://docs.python.org/3/library/turtle.html#:~:text=The%20turtle%20module%20is%20an,%20100%25%20compatible%20with%20it.)__

   * Una expresión (expression) es una combinación de valores, variables y operadores.
    * El intérprete evalúa expresiones
    * 2 + 2
  * Un enunciado (statement) es una unidad de código que tiene un efecto
    * age = 20

  * Orden de operaciones:
    * Parentesis
      * Exponente
        * Multiplicación
        * División
          * Adición
          * Substracción
  * PEMDAS 

  ## Funciones
  * En el contexto de la programación, una función es una secuencia enunciados (statements) con un nombre que realizan un cómputo
  * Una función tiene un nombre,parámetros (opcional) y valor de regreso (return value)(opcional)
  * Python incluye varias built-in functions en su [librería estándar](https://docs.python.org/es/3/library/). En el contexto de la programación, una función es una secuencia enunciados (statements) con un nombre que realizan un cómputo
  * Una función tiene un nombre,parámetros (opcional) y valor de regreso (return value)(opcional)
  * Python incluye varias built-in functions en su librería estándar. 

  * Otras funciones se pueden encontrar en módulos
    * Para utilizarlas es necesario importar el módulo
      * Ejmplo `import math`
    * Para declar una función, utilizamos el keyword `def`
      * Ejemplo `def my_fuction(first_arg, second_arg=None)`
    Las funciones se pueden componer.
      ```python
      def sum_two_numbers(x,y):
        return x + y


        other_function(sum_two_numers(3,4))
      ```
    * Los argumentos pueden ser posicionales (positional arguments) o con nombre (named arguments)
      * Los parámetros y variables son locales a la función
        * global keyword
      * Orden de ejecución
        * Arriba para abajo
        * Izquierda a derecha

         
## Estructuras condicionales

  * Una expresión boolena siempre evalúa como verdadero `(True)` o como falso `(False)`
  * Operadores de comparación
    * x = 2
    * y = 2
    * x == y
    * x != y
    * x > y
    * x < y
    * x >= y
    * x <= y

  ### Operadores lógicos
 **Operador lógico and**

  | p | q | and |    
  |----:| :------:|:------ |
  | T | T | T |
  | T | F | F |
  | F | T | F |
  | F | F | F |

  **Operador lógico or**
  | p | q | or |    
  |----:| :------:|:------ |
  | T | T | T |
  | T | F | T |
  | F | T | T |
  | F | F | F |

  **Operador lógico not**
  |  | q | not |    
  |----:| :------:|:------ |
  |  | T | F |
  |  | F | T |
  |  | T | F |
  |  | F | F |

* Ejemplo 

  ```python
  x = 2
  y = 3
  a = 5
  b = 7

  (x < y) and (a > b)     # True
  (x < y) and (a > b)     # False
  (x < y) or (a > b)      # True

  if x < y:
    print('x es menor que y')
  else:
    print('x no es menor que y')  # x es menor que y
  ```
  
# Uso de strings y ciclos

  ## Strings en Pyhton

  * Las cadenas (strings) es un tipo con comportamiento diferente a los `int`, `float` y `bool`.
      * Las cadenas son secuencias
      * Las secuencias se pueden acceder a través de un índice
        ```python
        apple = 'apple'
        apple[1]
        ```
      * Las cadenas (al igual que otras secuencias) tienen una longitud
        * Para saber la longitud de una secuencia, se puede usar la función `len`
          * `len(apple)`
        * En Python, los caracteres que componen un string se reutilizan a lo largo del programa
          * Esto ayuda a reducir la cantidad de memoria que necesita el programa
          * También significa que los strings deben ser inmutables
            ```python
            x = 'a'
            y = 'b'
            id(x) == id(y)
            ```
          

  ## Operaciones con strings
   
   * Los strings tiene varios métodos que nos sirven para manipularlas.
   * Algunos son:

  ```python  
    upper
    lower
    find
    startswith
    endswith
    capitalize
  ```
  * Operadores de pertenencia
    ```python
    in
    not in
    ```
  * Comparaciones entre strings
    * Las comparaciones son lexicográficas
    * Tener cuidado `'a'` y `'A'`  son diferentes.
  
  Otros `dir()` y `help()`. 

  ## Operaciones con strings y el comando Update

  ## Operaciones con strings y el comando Delete

  ## Operadores con strings

    #### Slices python

    * Python tine una de las sintaxis más poderosas para manipular secuencias.
    * Esta sintaxis se llama **slice** (rebanada en español)
      * Secuencia `[comienzo:final:pasos]`.

      ```python
      my_name = 'David'
      my_name[0]
      my_name[-1]
      my_name[0:3]
      my_name[::2]
    ```
  
## For loops

* Los **for** loops permiten ciclar a lo largo de una secuencia.
* Se usan cuando se quiere ejecutar un conjunto de instrucciones varias veces.
  * Esto tmabién se llama ´iteration`
* Se puede utilizar el keyword `continue` para saltarse los statements restantes y pasar a la siguiente iteración.

```python
for i in range(1000):
  print(i)
```
`range` es una secuencia de numeros.   

  ## While loop

  * Al igual que los `for` loops, los `while` loops sirven para iterar a lo largo de una secuencia.
  ```python
  def cuenta_regresiva(n):
    while n » 0:
      print(n)
      n -= 1
  ```
  ## While loops

  * Al igual que los for loops, los while loops sirven para iterar a lo largo de un secuela
    ```python
    def cuenta_regresiva(n):
      while n > 0:
        print(n)
        n -= 1
    ```
  * Los while loops se ejecutan de la siguiente manera:
    * Determinan si la condición es verdadera
    * Si es verdadera, vuelve a ejecutar el loop
    * Si es falsa, sal del bloque y continúa ejecuctando el programa
  * Se tiene que tener mucho cuidado para evitar un ifinite loop
  * Se puede utilizar el keyword break se se quiere salir anticipadamente del ciclo.
  

  ## Iterators and generators

  Aunque no lo sepas, probablemente ya utilices iterators en tu vida diaria como programador de Python. Un iterator es simplemente un objeto que cumple con los requisitos del Iteration Protocol (protocolo de iteración) y por lo tanto puede ser utilizado en ciclos. Por ejemplo,
```python
for i in range(10):
    print(i)
```
En este caso, la función range es un iterable que regresa un nuevo valor en cada ciclo. Para crear un objeto que sea un iterable, y por lo tanto, implemente el protocolo de iteración, debemos hacer tres cosas:
    • Crear una clase que implemente los métodos iter y next
    • `iter` debe regresar el objeto sobre el cual se iterará
    • `next` debe regresar el siguiente valor y aventar la excepción StopIteration cuando ya no hayan elementonexteclaramos una función y utilizamos el keyword yield en vez de return para regresar el siguiente valor en una iteración. Por ejemplo,
```python
def fibonacci(max):
  a, b = 0, 1
  while a < max:
      yield a
      a, b = b, a+b
```
Es importante recalcar que una vez que se ha agotado un generator ya no podemos utlizarlo y debemos crear una nueva instancia. Por ejemplo,
```python
fib1 = fibonacci(20)
fib_nums = [num for num in fib1]
...
double_fib_nums = [num * 2 for num in fib1] # no va a funcionar
double_fib_nums = [num * 2 for num in fibonacci(30)] # sí funciona
```

# Estructuras de datos

  ## Uso de listas
  * Como los strings, las listas son secuencias de valores.
    * En las listas, los valores pueden tener cualquier tipo.
      ```python
      [2, 4, 6]
      ['Colombia', 'Mexico', 'Argentina']
      ['tacos', 3, 'areoas', 6, 'chorizo', 9]
      ```
    * Las listas son mutables, a diferenic de los strings
      ```python
      my_list = [1, 2, 3]
      my_list[2] = 6
      ```
    * Los índeces de las listas, funcionan igual que los de los strings
    * Las listas se inician con `[]` o con la función `list`

    **Copiar una lista**

    ```python
    import copy

    # Copiar lista
    countries = ['Guatemala', 'Venezuela', 'Colombia', 'Argentina']
    global_countries = copy.copy(countries)

    # Asignamos un nuevo pais
    countries[0] = 'Honduras'
    countries
    ['Honduras', 'Venezuela', 'Colombia', 'Argentina']

    # Conserva los datos
    global_countries
    ['Guatemala', 'Venezuela', 'Colombia', 'Argentina']

    # for
    for country in countries:
      print(country)
 
    Honduras
    Venezuela
    Colombia
    Argentina
    ``` 

  ## Operaciones con listas

  * El operador `+ (suma)` concatena dos o más listas
    ```python
    a = [1, 2]
    b = [2, 3]
    a + b # [1, 2]
    ```
  * El opeador `* (multiplicación)` repite la misma lista
    ```python
    a = [1, 2]
    a * 2 # [1, 2, 1, 2]
  ```
  * Para añadir un elemento al final de listas, podemos utilizar el método `append`
  ```python
  a = [1, 2]
  a.append(2) # [1, 2]
  ```
  * Para eliminar el último elemento de la lista, podemos y utilizar el método `pop`
    * Este método, también regresa el valor que fue eliminado
    ```python
    a = [1, 2]
    b = a.pop[2]
    print(a)    # [1]
    print(b)     # 2
    ```
  * Para ordenar una lista, podemos utilizar el método `sort`
    ```python
    a = [3, 8, 1]
    a.sort() # [1, 3, 8]
    ```
  * Para eliminar elementos, también podemos utilzar el keyword `del`
    * `del` también con `slices`
    ```python
    a = [1, 2, 3]
    del a[-1]
  * Si sabes qué el elemento quieres eliminar, pero no su índice, puedes utilizar el método `remove`.
