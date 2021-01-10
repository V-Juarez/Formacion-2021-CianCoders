# Python
<p align="center"><a href=""><img src="https://www.python.org/static/community_logos/python-logo-master-v3-TM-flattened.png" width="600"></a></p>

# Tabla de contenido
- [¿Qué es la programación?](¿Qué-es-la-programación?)
- [¿Por qué programar con Python?](¿Por-qué-programar-con-Python?)
- [Operadores matemáticos](Operadores-matemáticos)
- [Variables y expresiones](Variables-y-expresiones)
- [Funciones](Funciones)
- []()
- []()
- []()

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
