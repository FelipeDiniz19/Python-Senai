#Range ()
 # Por ser muiot comum a criação de sequência numérica o Python criou uma função onde voce passa os criterios para tal sequência e ele a partir disso cria sua sequência
 #range(inicio,fim,incremento)

 #Inicio
 # A partir de qual número a sequência será iniciada
 
 #FIM
 # Em qual número será finalizado, mas o fim é sempre um número abaixo do qual foi colocado, se por exemplo voce colocar para finalizar no número ele irá no número 5 a contagem 

 #INCREMENTO
 # É onde voce pode escolher se quer contar de 2 em 2 , ou 3 em 3, ou se quer fazr uma contagem regressiva

#for numero in range(0,10,1):
# print(numero)

 # Crie um programa onde o usúario vai dizer quantas notas vão ser cadastradas, some as notas e tire uma média. No final fale se o aluno foi aprovado ou reprovado

quantidade = int(input("Digite a quantidade de notas: "))
soma = 0
 
for numero in range(0, quantidade):
  nota = float(input("Digite a nota: "))
  soma = soma + nota

media = soma / quantidade
print(f"Sua média é {media:.1f}")

if media >= 7:
 print("Aprovado")

elif media >=5 and media <=6.9:
 print("Recuperação")

else:
 print("Reprovado")