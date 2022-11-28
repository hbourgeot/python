#########################################
### Tipos de datos en python          ###
#########################################

print(type(6)) # int (entero)
print(type(6.5)) # float (flotante)
print(type(6j)) # complex (numero complejo)
print(type("")) # str (string)
print(type(True)) # bool (booleano)

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
print(2/2)

## Division exacta
print(2//2)

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
  print("5 es menor que 3")

## if-else
if 5 < 3:
  print("esta linea no se ejecuta")
else:
  print("esta linea si")

## if-elif-else (elif = else if)
if 5 < 3:
  print("esta linea tampoco se ejecutara")
elif 5 > 3:
  print("esta si se ejecutara")
else:
  print("como la anterior se ejecutó, esta no")

#########################################
### Ingreso de valores por consola    ###
#########################################

miVariable = input("Puedes colocar algo de mensaje para la entrada: ")
print(miVariable)