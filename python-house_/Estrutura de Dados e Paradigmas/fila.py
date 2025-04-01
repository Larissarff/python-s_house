'''

TIPOS DE ESTRUTURAS DE DADOS DE LISTAS LINEARES:

* FILAS -> 
    Caracteriza-se por, na extremidade onde se adiciona os itens, é oposta à extremidade onde se extrai itens.
    O primeiro a entrar é o primeiro a sair (FIFO - First In First Out)

    - operações básicas:
    enfileirar: incluir um elemento na fila.
    desenfileirar: retirar um elemento da lista.
    imprimir: imprime o tamanho da fila.
    
'''

# Exemplo de Pilha:
class No:
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None  # Ponteiro para o próximo nó

class Fila:
    def __init__(self):
        self.inicio = None  # Primeiro elemento da fila
        self.final = None   # Último elemento da fila
        self.tamanho = 0    # Quantidade de elementos na fila

    def is_empty(self):
        """Verifica se a fila está vazia."""
        return self.tamanho == 0

    def incluir(self, dado):
        """Adiciona um item no final da fila."""
        novo_no = No(dado)  # Cria um novo nó
        if self.is_empty():
            self.inicio = self.final = novo_no  # Primeiro elemento da fila
        else:
            self.final.proximo = novo_no  # O último nó aponta para o novo
            self.final = novo_no  # O novo nó vira o final da fila
        self.tamanho += 1  # Atualiza o tamanho da fila

    def remover(self):
        """Remove e retorna o item do início da fila."""
        if self.is_empty():
            raise IndexError("pop de fila vazia")
        
        dado = self.inicio.dado  # Obtém o item do primeiro nó
        self.inicio = self.inicio.proximo  # Move o início para o próximo nó

        if self.inicio is None:  # Se a fila ficou vazia, o final também deve ser None
            self.final = None
        
        self.tamanho -= 1  # Atualiza o tamanho da fila
        return dado

    def peek(self):
        """Retorna o item no início da fila sem remover."""
        if self.is_empty():
            raise IndexError("peek de fila vazia")
        return self.inicio.dado  # Retorna o item do primeiro nó

    def tamanho_fila(self):
        """Retorna o número de elementos na fila."""
        return self.tamanho


# Exemplo de uso:
fila = Fila()  # Instancia a fila
fila.incluir(10)
fila.incluir(20)
fila.incluir(30)

print(fila.remover())  # Vai imprimir 10
print(fila.peek())  # Vai imprimir 20
print(fila.remover())  # Vai imprimir 20
print(fila.tamanho_fila())  # Vai imprimir 1
