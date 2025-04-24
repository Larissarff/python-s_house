# Arquivos txt são universais e podem ser lidos por praticamente qualquer dispositivo ou sistema operacional

import os

texto = "Ciência de Dados é uma ótima alternativa para carreira."
texto = texto + " Esses profissionais costumam manipular python."
texto += " E, claro, devem ser proeficientes em Data Science"

"""
Dessa forma abaixo, criamos o arquivo cientista.txt utilizando o pacote os
"""
arquivo = open(os.path.join('C:/Users/Pichau/Downloads/Python/pythons_house/python-s_house-1/python-house_/manipulacao_de_arquivos/manipulacao_arq_txt/cientista.txt'), "w")

# método de gravar os dados no arquivo
for palavra in texto.split(): 
    # quando o split possui seus parênterses vazios, ele assume espaço como separação.
    arquivo.write(palavra + ' ')

arquivo.close()

# abrindo arquivo para leitura
arquivo = open('C:/Users/Pichau/Downloads/Python/pythons_house/python-s_house-1/python-house_/manipulacao_de_arquivos/manipulacao_arq_txt/cientista.txt', 'r')

conteudo = arquivo.read()
arquivo.close()
print(conteudo)
