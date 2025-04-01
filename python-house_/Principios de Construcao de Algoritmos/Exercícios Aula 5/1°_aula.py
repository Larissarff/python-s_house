# INTRODUÇÃO: 
#  Python - multiparadigma - multiplataforma

print("Hello, world!")

# int (inteiro): num = 10;
# float (ponto flutuante): num = 10.5;
# complex (complexo): Números complexos na forma a + bj: num = 1 + 2j;
# str (string): texto = "Olá, Mundo!"
# list (lista): Coleção ordenada e mutável de itens. lista = [1, 2, 3, "a", "b", "c"];
# tuple (tupla): Coleção ordenada e imutável de itens. tupla = (1, 2, 3, "a", "b", "c");
# range (intervalo): Sequência de números gerada a partir de um intervalo. intervalo = range(1, 10);
# dict (dicionário): Coleção não ordenada de pares chave-valor. dict = {"chave1": "valor1", "chave2": "valor2"}
# set (conjunto): Coleção não ordenada de itens únicos. conjunto = {1, 2, 3, 4, 5}
# frozenset (conjunto imutável): Conjunto imutável de itens únicos. conjunto_imutavel = frozenset([1, 2, 3, 4, 5])
# Bool : True ou False. resultado = True
# Tipo None NoneType: Ausência de valor ou valor nulo. lista = None;
# function: Funções definidas pelo usuário ou integradas


# PEP8 - boas praticas de programação em python
#exemplo de má pratica:

def main():

  #ler as entradas do usuário
  num1: int = int(input("Digite o primeiro numero: "))
  num2: int = int(input("Digite o segundo numero: "))

  # operação somar
  print(f"({num1} + {num2} = {num1} + {num2})")
  #operação subtrair
  print(f"({num1} - {num2} = {num1} - {num2})")
  # operação multiplicar
  print(f"({num1} * {num2} = {num1} * {num2})")
  # operação divisão (resultado inteiro0
  print(f"({num1} // {num2} = {num1} // {num2})")


# boas particas:
# def main() -> None: # informa que se trata de um procedimendo e não uma função, pois não retorna nada (-> None)
