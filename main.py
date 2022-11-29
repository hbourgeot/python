#########################################
### Tipos de datos en python          ###
#########################################

# print(type(45)) # int (entero)
# print(type(6.56645)) # float (flotante)
# print(type(6j)) # complex (numero complejo)
# print(type("")) # str (string)
# print(type(True)) # bool (booleano)

#########################################
### Variables en python               ###
#########################################

miVariable = "Hola mundo"

#########################################
### Constantes en python              ###
#########################################

MICONSTANTE = "hihi"

#########################################
### Operaciones aritméticas en python ###
#########################################

## suma
print(2+2)

## Resta
print(2-2)

## Division flotante
print(3/2)

## Division exacta
print(3//2)

## Multiplicacion
print(2*2)

## Exponenciacion
print(3**3)

#########################################
### Operadores de asignacion          ###
#########################################

## Asignacion
miVariable = 15
print(miVariable)

## Asignación de suma
miVariable += 5
# miVariable = miVariable + 5
print(miVariable)

## Asignación de resta
miVariable -= 10
print(miVariable)

## Asignacion de division flotante
miVariable /= 2
print(miVariable)

## Asignacion de division exacta
miVariable //= 5
print(miVariable)

## Asignacion de multiplicacion
miVariable *= 10
print(miVariable)

## Asignacion de exponenciacion
miVariable**=2
print(miVariable)

#########################################
### Condicionales en python           ###
#########################################

## if
if 5 > 3:
  print("5 es mayor que 3")

## if-else
if 5 < 3:
  print("esta linea no se ejecuta")
else:
  print("esta linea si")

## if-elif-else (elif = else if)
if 10 != 10:
  print("esta linea tampoco se ejecutara")
elif 5 > 3:
  print("esta si se ejecutara")
elif 5 < 3:
  print()
else:
  print("como la anterior se ejecutó, esta no")

#########################################
### Ingreso de valores por consola    ###
#########################################

miVariable = input("Puedes colocar algo de mensaje para la entrada: ")
print(miVariable)

#########################################
### Arreglos en python                ###
#########################################

### Las listas son arreglos mutables
lista = ["Hola", "Mundo", "Protocolo", "Sharon", "elibeth", 245354]
print(lista)

## Metodos de una lista
lista.pop()
print(lista)
lista.append("Henrry")
print(lista)

lista.clear()
print(lista)

### Las tuplas son arreglos inmutables
tupla = ("Elibeth", "Anthony")

## Las tuplas no tienen metodos como .pop(), ya que una vez que las declaras, no se pueden modificar
print(tupla.count("Luis"))

#########################################
### Conversión de valores en python   ###
#########################################

numero = int(input("Ingrese nro: "))
print(numero, type(numero))

#########################################
### Bucles en python                  ###
#########################################

### While
i = 0
while i < 5:
  i += 1 # en python no existe el incremento y decremento
  if i == 3:
    continue
  print(i)

### For

## Iterando en base a una lista
usuarios = ["chanchito feliz", "felipe", "roberto", "nicolas"]
for usuario in usuarios:
  print(usuario)

## Iterando en base a un string
usuario = "henrry"
for i in usuario:
  print(i)

### For común
for x in range(0, 5, 1):
  print(x)
  
'''
  La función range admite 3 parámetros:
  1. l primero es el valor en el que comenzará x, en este caso, 0.
  2. El segundo es hasta cuándo se va a iterar el bucle.
  3. El último es de cuánto en cuánto queremos iterar, ahora el bucle va a iterar de uno en uno.
  
  El bucle que acabas de ver, es igual que hacer esto en C++
  for(int i = 0; i < 5; i++)
'''

#########################################
### Funciones en python               ###
#########################################

def miFuncion(): # declaración de una función
  print("Mi primera funcion")

miFuncion() # llamada de una función

def imprimeDato(*nombre): # función con N cantidad de argumentos
  print("El nombre completo es:", nombre)
  
imprimeDato("Henrry","Francisco","bourgeot", "Silva")

def nombreApellido(apellido, nombre): # funcion con dos argumentos
  print(nombre, apellido)

nombreApellido(nombre="chanchitp", apellido="feliz") # llamada de una funcion con parametros, se pueden asignar valores a sus argumentos desde cualquier lado siempre y cuando se coloque el nombre del argumento

def conValoresDefault(defecto = "Hola mundo"): # asignas un valor por defecto si no es pasado.
  print(defecto)

conValoresDefault() # sin parámetros
conValoresDefault("Hi!") # con parámetros

def concatenaNombres(lista): # funcion que recibe una lista
  i = ""
  for el in lista:
    i = i + el + ' '
  
  return i

# al definir una función que retorna valores, se debe asignar a una variable
nombre = concatenaNombres(["Henrry", "Bourgeot"])
print(nombre)