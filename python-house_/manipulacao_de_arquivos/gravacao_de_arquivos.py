# Abrindo o arquivo para gravação (alteração)
arq2 = open("C:\\Users\\Pichau\\Downloads\\Python\\pythons_house\\python-s_house\\python-house_\\manipulacao_de_arquivos\\arquivos\\arquivo2.txt", "w") # w = write

# como abrimos o código para gravação, ele não é habilitado para leitura


# gravando no arquivo
arq2.write("Eu nao sei pra onde ir, sinto um vazio por dentro \nMe escondo pra fugir desse sentimento")


arq2.write("\nGuardei meus segredos \nRepeti meus erros mas ainda estou aqui")


arq2 = open("C:\\Users\\Pichau\\Downloads\\Python\\pythons_house\\python-s_house\\python-house_\\manipulacao_de_arquivos\\arquivos\\arquivo2.txt", "r") # assim para visualizar
# o conteúdo do arquivo, habilitamos o modo de leitura

print(arq2.read()) 
