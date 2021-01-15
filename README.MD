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
  * Para añadir un elemento al final de listas, podemos utilizar el método `append`.

  ```python
  a = [1, 2]
  a.append(2) # [1, 2]
  ```
  * Para eliminar el último elemento de la lista, podemos y utilizar el método `pop`.

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
    ```
  * Si sabes qué el elemento quieres eliminar, pero no su índice, puedes utilizar el método `remove`.

  ## Diccionarios
  
  * Un diccionario es similar a un lista en el sentido de que se puede acceder a través de índeces (en el diccionario se llaman llaves)

    * En la lista de los índices tienen que ser enteros.

    * En el diccionario pueden ser casi cualquier tipo

  * Un diccionario es una asociación entre llaves `(keys)` y valores `(values)`.

  * Los diccionarios se inicializan con `{}` o con la funcion `dict`.
  
  ```python
  productos = {}
  prodcutos{`leche`} = 23.50
  ```
  ### Métodos de un diccionario
    
  * Existen varias formas de ciclar a lo largo de un diccionario
  
  ```python
  for key in my_duct_keys():
    pass

  for value in my_dict_values():
    pass

  for key, value in my_dict_items():
    pass
  ```

  ## Tuplas y conjuntos

  * Las tuplas `(tuples)` son similares a las listas.
    * La mayor diferenica es que son inmutables.
  * Lo que define a un tuple es que sus valores están separados por comas.
    * Es buena práctica utilizar un paréntesis también para ayudar a la legibilidad
    ```python
    tup = 1, 3, 4
    tup = (1, 2, 3)
    ```
  * También pidemos utilizar la función `tuple`.
  * Un uso muy común es utilizarlas para regresar más de un valor en una función `retrun(students, teachers)`
  
  **Conjuntos**

  * Los conjuntos `(sets)` son una colección sin orden que no permite elementos duplicados.
  * Los `sets` se inicializan conla función `set`.
  * Para anñadir elementos utilizamos el método `add`
  * Y para eliimarlos, el método `remove`.

  ## Módulo Collections

  El módulo collections nos brinda un conjunto de objetos primitivos que nos permiten extender el comportamiento de las built-in collections que poseé Python y nos otorga estructuras de datos adicionales. Por ejemplo, si queremos extender el comportamiento de un diccionario, podemos extender la `clase UserDict`; para el caso de una lista, extendemos `UserList`; y para el caso de `strings`, utilizamos `UserString`.

Por ejemplo, si queremos tener el comportamiento de un diccionario podemos escribir el siguiente código:
```python
class SecretDict(collections.UserDict):

   def _password_is_valid(self, password):
        …

    def _get_item(self, key):
        … 

    def __getitem__(self, key):
         password, key = key.split(‘:’)
         
         if self._password_is_valid(password):
              return self._get_item(key)
         
         return None

my_secret_dict = SecretDict(...)
my_secret_dict[‘some_password:some_key’] # si el password es válido, regresa el valor
```
Otra estructura de datos que vale la pena analizar, es namedtuple. Hasta ahora, has utilizado tuples que permiten acceder a sus valores a través de índices. Sin embargo, en ocasiones es importante poder nombrar elementos (en vez de utilizar posiciones) para acceder a valores y no queremos crear una clase ya que únicamente necesitamos un contenedor de valores y no comportamiento.
```python
Coffee = collections.NamedTuple(‘Coffee’, (‘size’, ‘bean’, ‘price’))
def get_coffee(coffee_type):
     If coffee_type == ‘houseblend’:
         return Coffee(‘large’, ‘premium’, 10)
```
El módulo collections también nos ofrece otros primitivos que tienen la labor de facilitarnos la creación y manipulación de colecciones en Python. Por ejemplo, `Counter` nos permite contar de manera eficiente ocurrencias en cualquier iterable; `OrderedDict` nos permite crear diccionarios que poseen un orden explícito; deque nos permite crear filas `(para pilas podemos utilizar la lista)`.

En conclusión, el módulo collections es una gran fuente de utilerías que nos permiten escribir código más “pythonico” y más eficiente.

  ## Comprehensions

  * Comprenhensions son constructos que nos permite generar secuencias a partir de otras secuencias.

  * List Comprehension
    * `[element for element in element_list if element_meets_condition]`
  * Dictionary Comprehension
    + `{key: element for element in element_list if element_meets_condition}`
  * Set Comprehension
    * `{element for element in element_list if element_meets_condition}`

**List Comprehension**
```python
lista_de_numeros = list(range(100))

# consola
>>>>lista_de_numeros
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31,
32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90,91, 92, 93, 94, 95, 96, 97, 98, 99]

------------------------------------------------------------
pares = [numero for numero in lista_de_numeros if numero % 2 == 0]

# console
>>>> Pares
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98]

**Dictionary Comprehension**

  ```python
  student_uid = [1, 2, 3]
  students = ['Juan', 'Jose', 'Larsen']
  Students_whith_uid = {uid: student for uid, student in zip(student_uid, students)}

  # consola
  >>>> students_with_uid
  {1: 'Juan', 2: 'Jose', 3: 'Larsen'}
  ```

**Set Comprehension**

```python
import random
random_numbers = []
for i in range(10):
  random_numbers.append(random.randint(1, 3))

# console
>>> random_numbers
[2, 2, 3, 3, 2, 1, 3, 3, 1, 1]

non_repeated = {number for number in random_numbers}

# console
>>> non_repeated
{1, 2, 3}
```