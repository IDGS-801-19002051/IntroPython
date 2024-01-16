print("suma de numeros")

num1=int(input("dame n1: "))
num2=int(input("dame n2: " ))

if num1 > num2:
  print("el {} es mayor que el {}".format(num1,num2))
else:
  print("el {} es mayor que el {}".format(num2,num1))

print("-----------pedir una edad-----------")
edad=int(input("Ingresa tu edad"))
if edad>10:
  print("Eres mayor de edad")
elif edad== 18:
  print("eres mayor de edad")
else:
  print("No eres mayor de edad")