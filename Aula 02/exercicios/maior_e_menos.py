numero_1 = input ("digite primeiro numero: ")
numero_1 = int (numero_1)
numero_2 = input ("digite segundo numero: ")
numero_2 = int (numero_2)
numero_3 = input ("digite terceiro numero: ")
numero_3 = int (numero_3)

if numero_1 >= numero_2 >= numero_3 :
    maior = numero_1

elif numero_2 >= numero_1 >= numero_3 :
    maior = numero_2

else:
    maior = numero_3

if numero_1 <= numero_2 <= numero_3 :
    menor  = numero_1

elif numero_2 <= numero_1 <= numero_3 :
    menor = numero_2

else:
    menor = numero_3

print (f"O maior numero é : {maior}")
print(f"O menor numero é : {menor}")