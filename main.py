bienvenida = input()
print("Hola que tal, yo soy Nico y voy a ser tu asistente para ayudarte a recordar tus tareas")
usuario = str(input("Como te llamas: "))
datos = set()
datos.add(usuario)

recordatorio = []

def Menu():
  menu = "Eliga una de las opciones:\n \t 1)Ingresar un recordatorio.\n \t 2)Mirar mis recordatorios. \n \t 3)Eliminar un recordatorio.\n \t 4)Editar un recordatorio.\n \t 5)Salir."
  return menu

def agregar_recordatorio():
  informacion = str(input("Ingrese el nombre de su recordatorio y toda la informacion adicional que usted desee:\n"))
  print(informacion)

  menu_dos ="Seleccione una opcion:\n \t Si los datos son correcto digite 1.\n \t Si desea editar estos datos precione 2."
  print(menu_dos)
  opcion_dos = int(input("-> "))

  entrada = True
  while entrada:
    if opcion_dos == 1:
      entrada = False
    elif opcion_dos == 2:
      while opcion_dos == 2:
        informacion = str(input("Ingrese el nombre de su recordatorio y toda la informacion adicional que usted desee:\n"))
        print(informacion)

        menu_dos ="Seleccione una opcion:\n \t Si los datos son correcto digite 1.\n \t Si desea editar estos datos precione 2."
        print(menu_dos)
        opcion_dos = int(input("-> "))
      entrada = False
    else:
      print("Opcion ingresada es incorrecta, por facor seleccione una opcion:\n \t Si los datos son correcto digite 1.\n \t Si desea editar estos datos precione 2.")
      opcion = int(input(""))
      loop = True
      while loop:
        if opcion == 1 or opcion == 2:
          loop = False
        else:
          print("Opcion ingresada es incorrecta, por facor seleccione una opcion:\n \t Si los datos son correcto digite 1.\n \t Si desea editar estos datos precione 2.")
          opcion = int(input(""))

  recordatorio.append(informacion)
  return "Su recordatorio fue ingresado con exito!!\n"

def Mirar_mis_Recordatorios(recordatorio):
  recordatorio2 = list(recordatorio)
  for i in range(len(recordatorio)):
    print(i+1, "> ",recordatorio2[0])
    recordatorio2.pop(0)
  
  return "Estos son todos tus recordatorios!!\n"

def Eliminar_un_Recordatorio(lista, recordatorio):
  recordatorio2 = list(recordatorio)
  cont = 0
  for i in range(len(lista)):
    print(i+1, "> ",recordatorio2[0])
    recordatorio2.pop(0)
    cont += 1

  a = int(input("Ingresar el número del que desea eliminar: "))
  n = a - 1

  if len(recordatorio) > 0:
    recordatorio.pop(n)
    return "Eliminado con éxito!!"
  else:
    return "Usted no tiene recordatorios!!"

def Editar_un_Recordatorio(lista, recordatorio):
  recordatorio2 = list(recordatorio)
  cont = 0
  for i in range(len(lista)):
    print(i+1, "> ",recordatorio2[0])
    recordatorio2.pop(0)
    cont += 1

  a = int(input("Ingresar el número del que desea eliminar: "))
  n = a - 1
  mensaje_nuevo = str(input("Ingrese la informacion del recordatorio de nuevo: "))
  if len(recordatorio) > 0:
    recordatorio[n] = mensaje_nuevo
    return "Editado con éxito!!"
  else:
    return "Usted no tiene recordatorios!!"

def Salir():
  print("Nos vemos pronto!!")
  bienvenida = input()
  return "Hola como va"  

def Opciones(opcion):
  if opcion != 1 and opcion != 2 and opcion != 3 and opcion != 4 and opcion != 5:
    print("La opcion ingresa no es correcta.") 
  elif opcion == 1:
    return agregar_recordatorio()
  elif opcion == 2:
    lista = list(recordatorio)
    return Mirar_mis_Recordatorios(recordatorio)
  elif opcion == 3:
    lista = list(recordatorio)
    return Eliminar_un_Recordatorio(lista, recordatorio)
  elif opcion == 4:
    lista = list(recordatorio)
    return Editar_un_Recordatorio(lista, recordatorio)
  else:
    return Salir()


Entrada_Al_Programa = True

while Entrada_Al_Programa:
  print(Menu())
  opcion = int(input("-> "))
  print(Opciones(opcion))
