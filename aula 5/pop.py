#pop
#com o pop exluimos da lista, mas ele ainda continua armazenado

alunos = ['Amanda','Rodrigo','Davi', 'Paula']
print(alunos)
excluir = int(input('Escreva a posição do aluno que deseja excluir: '))

excluido = alunos.pop(excluir)

print(excluido)
print(alunos)