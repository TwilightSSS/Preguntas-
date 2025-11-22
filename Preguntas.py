
class python:
  
   def __init__(self, name):
      self.name = name
   
   
   def get_name(self):
      return self.name
   
   def set_name(self): 
      nombre = input("Ingresar un nombre: ").capitalize()
      self.name = nombre

   



programador1 = python("")



programador1.set_name()
print(f"Hola {programador1.get_name()} empecemos ")






points = 0
def preguntas():
   p1()
   

def p1():
   global points 
    
   while True: 

      
      print(f"\nExamen de Programación conceptos para enteder la teria (Se sumaran +5 puntos por acertar y -5 al equivocarse) Suerte!! "
             "Pregunta 1: ¿Que es python?\n")

      n1 = print("1º Un lenguaje de programación interpretado, de tipado dinámico y multiparadigma, diseñado por Guido van Rossum en 1991.")   
      n2 = print("2º Un entorno de ejecución que compila bytecode directamente al kernel del sistema operativo mediante optimización JIT avanzada.")
      n3 = print("3º Un framework que extiende la máquina virtual JVM para permitir scripting de alto rendimiento.")     

      
      
      
      try:
         op = int(input("\nOpciones de 1,2,3 escojer: "))
         if op==1:
            points +=5
            print(f"\nCorrecto!! ganaste {points} puntos")
            while True:
               pre2 = input("\nIngresar solo 'si' o 'no' para ir a pregunta 2 : ").lower()
               if pre2 == 'si':
                  p2()
                  return
               elif pre2 == 'no':
                  print("Saliste del programa baay.")
                  return
               else:
                  print("Ingresar 'si' ó 'no' ")
                  continue

            
            
         elif op!=1:
               points-=5
               print("\nIncorrecto ")
               print(f"Points: {points}")

               while True:
                  op2 = input("¿Intentar de nuevo? Pregunta 1º 'si' ó 'no': ").lower()
                  
            
                  if op2=='si': 
                     print("\nOk pregunta 1 otra vez. Vamos!!\n")
                     break
               

                  elif op2=='no':  
                     print("Ok Chao..(1)")
                     return 
                  else:print("Escojer 'si' o 'no'")
                  continue #
                  
      except ValueError as e:
         print(f"\nIngresar 1,2,3 no otro caracter error(1) -> {e}")
         break


def p2():
   global points
   # ------------------------------------------------------------------ Pregunta 2 ---------------------------------------------------------
   while True:
      print(f"\nº Pregunta: Que es una variable?\n")  
      n1 = print("1º Un archivo interno del sistema operativo que guarda temporalmente el estado del programa durante su ejecución.")
      n1 = print("2º Un componente del procesador encargado de gestionar operaciones aritméticas y lógicas mediante registros dedicados.")
      n1 = print("3º Un nombre simbólico asociado a un espacio de memoria capaz de almacenar un valor que puede cambiar durante la ejecución del programa.")
   
      try:
         op = int(input("\nOpciones de 1,2,3 escojer: "))
         if op==3:
            points +=5
            while True:
               pre3 = input(f"\nNiice ganaste +5 en total {points} puntos ¿Ir a pregunta 3? 'si' ó 'no': ").lower()
               if pre3 =='si':
                  p3()
                  return 
               elif pre3=='no':
                  print("Saliste del programa adios..")
                  return
               else:
                  print("Ingresa solamente 'si' ó 'no' ")
                  continue
         elif op!=3:
            points-=5
            print(f"Incorrecto!! perdiste {points} puntos.")
            while True:
               op2 = (input("Intentar de nuevo Pregunta 2º 'si' ó 'no': " ))
               if op2=='si':
                  break 
               elif op2=='no':
                  print("bay")
                  return
               else:
                  print("Ingresar solo 'si' o 'no' ")
                  continue

      except ValueError as e:
         print(f"Ingresa valores 1,2,3 no caracteres error(2) -> {e}")

      
            

def p3():
   global points
   while True:
      print(f"\n3ºera Pregunta: Que es un condicional?\n")
      n1 = print("1º Una instrucción del compilador que reescribe el código en tiempo de compilación mediante optimizaciones heurísticas para eliminar expresiones redundantes.")
      n2 = print("2º Una estructura de control que permite ejecutar diferente código dependiendo de si una expresión booleana es verdadera o falsa. ")
      n3 = print("3º Una operación aritmética que compara valores a nivel binario sin alterar el flujo del programa.") 

      while True:
         try:
            op = int(input("\nIngresa que opción es de 1 ,2 ,3 : "))
            if op==2:
                  points+=5
                  print(f"\nCorrecto!! Ganas +5 queudas con un total de {points} puntos")
                  a = programador1.get_name().upper() 
                  print(f"\n\nGracias por participar amigo {(a)} te llevaste todos los punto total {(points)}\n\n")
                  return
            elif op==1 or op==3:
                  print(f"Incorrecto!! pierdes -5 puntos total {points-5} puntos")
                  return
            else:
                  print("Ingresa las opciones de 1,2,3 ")
                  continue
         
         except ValueError as e:
            print(f"Error ingresaste otro caracter que no esta en las opciones errror {e}")
            continue
            


preguntas()