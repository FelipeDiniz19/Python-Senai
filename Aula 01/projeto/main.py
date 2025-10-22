nome_filme = "Harry Potter"
sala_cinema = "sala dos pecinhas"
duracao = 120
quantidade_pessoas = 250
valor_ingresso = 49.99
valor_meia_ingresso = valor_ingresso / 2
print(f"Venham assistir ao filme {nome_filme} na {sala_cinema}")
print(f"Esse filme tem a duracao de {duracao} minutos e o valo inteiro do ingresso e de R${valor_ingresso}")
print(f"E o valor ingresso como meia e de R${valor_meia_ingresso}")

quantidade_ingressos = input("Quantos ingressos voce quer comprar: ")
quantidade_ingressos = int(quantidade_ingressos)

valor_final = quantidade_ingressos * valor_ingresso
print(f"Voce comprou {quantidade_ingressos} ingressos por R${valor_final}")