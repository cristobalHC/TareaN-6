lista = []
vocales = "aeiouAEIOU"
consonantes = "bcdfghjklmnñpqrstvwxyzBCDFGHJKLMNÑPQRSTVWXYZ"

palabra = input("ingrese palabra para agregar a lista: ")
print("(presione enter para finalizar el ingreso)")

while palabra != "":
    lista.append(palabra)
    palabra=input("ingrese palabra para agregar a la lista: ")
    print("(presione enter para finalizar el ingreso)")

for palabra in lista:
    V=0
    c=0
    print(palabra)
    for letra in palabra:
        if letra in vocales:
            V=V+1
        if letra in consonantes:
                C=C+1
            
    print("el numero de vocales de la palabra es: ",V)
    print("el numero de consonantes de la palabra es: ",C)
    print(" ")