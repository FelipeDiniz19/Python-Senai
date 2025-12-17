#Listas
#Em Python, uma lista (list) é uma sequência ordenada de valores, que são identificados por um índice. Estes valores, que compõem uma lista, são chamados de elementos ou itens. 
# Listas são estruturas de dados muito similares às strings, que por sua vez são sequência de caracteres, apenas. A diferença é que os elementos de uma lista podem ser de qualquer
# tipo, ou seja, podem ser homogêneos (todos os valores do mesmo tipo) e heterogêneos (valores com tipos distintos).

#Diferentemente das strings, uma lista é também uma sequência mutável e dinâmica. Uma vez que sejam criadas, é possível:

#* Alterar o valor de um ou mais elementos.
#* Os elementos podem ser adicionados, removidos ou substituídos.

#variável = [item1, item2, ...]

#A sintaxe para acessar os elementos de uma lista é por meio do operador [], especificando o índice (posição) do elemento a ser acessado (ex.: [0] e [1]) e sempre com o 
# primeiro elemento no índice 0. Também podemos utilizar índices negativos e o conceito de slicing (faixa de índices), que nos retorna uma sub-lista.

lista_de_compras = ['Arroz',
                         20,
                         2.40,
                        True,
                         None]

print (lista_de_compras)
type(lista_de_compras[4])

print(len(lista_de_compras))
