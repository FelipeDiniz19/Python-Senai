# Estrutura de repetição
# Ao desenvolver uma apliação , é comum depararmos com a necessidade de execuatar uma mesma instrução por repetidas vezes. Para tanto, as 
# linguagens de programação possuem as chamadas estruturas de repetição, A primeira delas, o while, nos permite repetir a execução de um 
# bloco de código enquanto uma determianada condição for verdadeira. A segunda estrutura de repetição é o for... in, que permite executar um bloco
# de código para cada elemento de uma sequência

#ESTRUTURA for in
# Em python, a estrutura de repetição for.. in permite executar um bloco de código repetidas vezes, sendo uma repetição para cada elemento em uma sequência. Em outras palavras
#ele permite percorrer(iterar) uma sequência iterável.
#a estrutura de código for..in repetirá um determinado bloco de código por um número definido de vezes, que é dado pelo tamanho da sequêcia que será percorrido
#for <item> in <sequêcia>:

palavra = str(input("Digite um texto: "))

for Letra in palavra:

 Nome = str(input("Digite seu nome: "))
 idade = int(input("Digite sua idade:  " ))
 curiosidade = str(input( "Digite uma curiosidade sobre voce:  "))

 print(f"CADASTRO CONCLUIDO \nNome:  {Nome} \nIdade:  {idade} anos \nCuriosidade:  {curiosidade}")     

