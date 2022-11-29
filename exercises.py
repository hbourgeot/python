# dato = input("Ingrese dato: ")

# lista = ["Hola", "mundo", "chanchito", "feliz", "dragones"]

# if lista.count(dato) > 0:
#   print("El dato existe", dato)
# else:
#   print("No existe", dato)

error = 0
simbolo: str
res: float
try:
  primero = int(input("ingrese el 1er numero: "))
  segundo = int(input("ingrese el 2do numero: "))
  simbolo = input("Ingrese el simbolo")
except:
  error = 1
  
if error:
  print("Ingresaste algo mal, no seas bruto.")
  exit()
else:
  if simbolo == "-":
    res = primero - segundo
  elif simbolo == "+":
    res = primero + segundo
  elif simbolo == "*":
    res = primero * segundo
  elif simbolo == "/":
    res = primero // segundo
  
  print("Resultado: ", res)