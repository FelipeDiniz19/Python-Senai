

print("=== Pagamento ===")


valor = input("Digite o valor da sua compra: R$")
valor = int (valor)


print("""
Escolha uma das opções abaixo:
1. À vista Dinheiro
2. À vista Cartão
3. À vista PIX
4. 2x no Cartão
5. 3x ou mais no Cartão
""")


opcao = input("Opção: ")
opcao = int (opcao)


if opcao == 1:
    valor_final = valor * 0.90   
    print(f"Calculando opção: {opcao}")
elif opcao == 2:
    valor_final = valor * 0.98   
    print(f"Calculando opção: {opcao}")
elif opcao == 3:
    valor_final = valor * 0.75  
    print(f"Calculando opção: {opcao}")
elif opcao == 4:
    valor_final = valor * 1.00   
    print(f"Calculando opção: {opcao}")
elif opcao == 5:
    valor_final = valor * 1.20  
    print(f"Calculando opção: {opcao}")
else:
    print("Opção inválida!")
    exit()


print(f"O seu produto de R${valor:.2f} com a opção {opcao} vai custar no final R${valor_final:.2f}")
