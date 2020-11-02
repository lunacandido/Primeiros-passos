### lista
d=[2, "sapo", ["mariposa","grilo", 3], [6, 8]]
print(d[0], d[1],d[2], d[3])
print(d[2][1])
### função len (retorna o numero de elemento que eu tenho na lista)
print(len(d))
d[0] = 15 ### modificando o 1 elemento
print(d)
## soma de listas 
C = [1,2,3] + [4,5,6]
print(C)
### repetição
print(C*2)
### append adiciona elemento no final da lista
C.append(7)
print(C)
### método extend
C.extend([8,9,10])
print(C)
### fatiando a lista
lista = [1,2,3,4,5,6,7,8,9,10]
print(lista[3:7])
