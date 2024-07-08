# Practica N 1 Patricia Villanueva Caba


#Pregunta 1
#Crear un programa que lea por teclado una cadena y un carácter, y reemplace todos 
#los dígitos en la cadena por el carácter

#cadena = input("Introduzca la cadena: ")
#caracter = input("Digite el caracter: ")
#nueva_cadena = ''
#for letra in cadena:
#    if letra.isdigit():
#        nueva_cadena += caracter
#    else:
#        nueva_cadena += letra

#print("Cadena original:", cadena)
#print("Cadena modificada:", nueva_cadena)

#Pregunta 2
# Crea un programa python que lea una cadena de caracteres y muestre la siguiente 
#información:
# La primera letra de cada palabra

#cadena=input("introduzca la cadena de caracteres: ")
#palabras= cadena.split()
#abreviatura = "".join([palabra[0].upper() for palabra in palabras])

#print("La abreviatura es:", abreviatura)


#Pregunta 3
# Escribir un programa python que dado una palabra diga si es un palíndromo. Un 
# palíndromo es una palabra, número o frase que se lee igual hacia adelante que hacia 
# atrás. 

#palabra=input("introduzca la palabra: ")
#if palabra== palabra[::-1]: 
#    print("Es palíndromo") 
#else: print("No es palíndromo")

# Pregunta 4
# Crear un programa que lea por teclado dos cadenas A y B y mostrar si es ENAGRAMA, 
# si es que la cadena A es anagrama de la cadena B.
# Se dice que una cadena es anagrama de otra si, usando todas los caracteres de la 
# primera y añadiendo o quitando espacios, se puede llegar a la otra cadena

#cadena_a=input("introduzca la cadena A: ")
#cadena_b=input("introduzca la cadena B: ")
#cadena_a = cadena_a.replace(" ", "")
#cadena_b = cadena_b.replace(" ", "")

#if sorted(cadena_a) == sorted(cadena_b):
 #   print("Las cadenas son anagramas")
#else:
 #   print("Las cadenas no son anagramas")


#Pregunta 5
#programe un procedimiento que reciba de parámetros una cadena S y un carácter C 
# e imprima cuantas veces aparece el caracter C en la cadena S.

#cadena=input(" introduzca una cadea: ")
#caracter=input("Introduzca un caracter: ")
#cont=0
#for letra in cadena:
 #   if letra == caracter:
  #      cont += 1
#print(f"El carácter {caracter} aparece {cont} veces en la cadena {cadena}")


#Pregunta 6
#Escriba un programa que pida un número entero mayor que cero y que escriba sus 
#divisores.

#num=int(input("introduzca el numero entero mayor que cero: "))
#print("sus divisores son: ")
#for i in range(1, num+1):
#    if num % i == 0:
#        print(i)


#Pregunta 7
# Escriba un programa que pregunte cuántos números se van a introducir, pida esos 
#números y escriba cuántos negativos ha introducido.

#numeros = int(input("¿Cuántos valores va a introducir? "))
#negativos = 0

#for i in range(numeros):
#    num = float(input("Introduzca un número: "))
#    if num < 0:
#        negativos += 1

#print("Ha introducido", negativos, "números negativos.")


#Pregunta 8
#escribir un programa python que dado un número diga si es un perfecto o no. Se 
#dice que un numero perfecto si al invertir los dígitos de un número es el mismo al 
#número original.

num=input("digite el número: ")
num_invertido = num[::-1]
if num == num_invertido: 
    print("El número ingresado es un número perfecto.") 
else: 
    print("El número ingresado no es un número perfecto.")

