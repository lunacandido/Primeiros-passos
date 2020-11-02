### strings
### indexação
palavra = 'homem aranha'
print(palavra[4])
###fatiamento 
print(palavra[1:6])
###operador in
print('aranha' in palavra)
###comparação
print(len('homem') > len('aranha'))
print(max(palavra))
print(min(palavra))
###alguns métodos para strings
print(palavra.upper()) ### passar para caixa alta
print(palavra.lower())  ### passar para caixa baixa
print(palavra.isupper())    ### true se estiver na caixa alta
print(palavra.islower())    ### true se está na caixa baixa
print(palavra.capitalize())   ### 1 letra maiuscula
print(palavra.title()) #### coloca a 1 letra de cada palavra maiuscula
print(palavra.count("a")) ### conta a ocorrencia de uma letra
print(palavra.startswith("h")) ## ve se começa com uma determinada letra
print(palavra.endswith("a")) ## ve se termina com determinada letra
print(palavra.find("aranha")) ### ve se a string esta dentro de outra e da a posição
print(palavra.rfind("aranha")) ### mesma coisa começando ao contrário
print(palavra.strip()) ## remove espaço em branco do inicio e do fim
print(palavra.isalpha()) ### true se tiver apenas letras
print(palavra.isdigit()) ### true caso for numero

