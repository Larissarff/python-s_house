# Lendo arquivos - Aula 1

# abrir o arquivo para modo leitura 
# ideal é colocar o caminho absoluto e com aspas duplas, para que não seja interpretado como escape
arq1 = open("C:\\Users\\Pichau\\Downloads\\Python\\pythons_house\\python-s_house\\python-house_\\manipulacao_de_arquivos\\arquivos\\arquivo1.txt", "r")

# Lendo arquivo
print(arq1.read())

# contar o numero de caracteres
print(arq1.tell())

# retornar para o início do arquivo
print(arq1.seek(0,0))

# lendo apenas os primeiros 17 caracteres apenas
print(arq1.read(17))

# lendo o restante do arquivo
print(arq1.read())

