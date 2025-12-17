#del
#para excluir uma informação da lista utilizamos o del

alunos = ['Amanda','Rodrigo','Davi','Paula']
print(alunos)
excluir = int(input('Esreve a posição do aluno que deseja excluir: '))

del alunos[excluir]
print(alunos)