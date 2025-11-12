nome_cliente = input("Insira seu nome:"). title()
idade_cliente = input("Insira sua idade:")
idade_cliente = int(idade_cliente)
nome_filme = "As branquelas"
valor_ingresso = 49.99
valor_meia_ingresso = valor_ingresso/ 2


print(f"Seja bem-vindo (a) {nome_cliente}")
print(f"O filme que está em cartaz é {nome_filme}")
print(f"O ingresso inteiro é R$ {valor_ingresso} e o meio é R$ {valor_meia_ingresso:.2f}")

quantidade_ingressos = input("Insira a quantidade de ingressos: ")
quantidade_ingressos = int(quantidade_ingressos)    

if idade_cliente <= 24 or idade_cliente >= 60:
    valor_final = quantidade_ingressos * valor_meia_ingresso
   

else: 
    valor_final = quantidade_ingressos * valor_ingresso
    

if quantidade_ingressos <= 3:
    valor_final *= 0.95

elif quantidade_ingressos <= 5:
    valor_final *= 0.90

elif quantidade_ingressos <= 10 :
    valor_final *= 0.80

else:
 valor_final *=0.70

print(f"sua compra saiu o total de R$ {valor_final:.2F}")