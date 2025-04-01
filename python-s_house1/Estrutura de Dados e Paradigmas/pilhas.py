'''

TIPOS DE ESTRUTURAS DE DADOS DE LISTAS LINEARES:

* PILHAS -> 
    Caracteriza-se por, na extremidade onde se adiciona os itens, é a extremidade onde se extrai itens.
    O último a entrar é o primeiro a sair (LIFO - Last In First Out)

    - operações básicas:
    empilhar: incluir um elemento no topo da pilha.
    desempilhar: retirar um elemento do topo da lista.
    imprimir: imprime o tamanho da pilha.
    
'''

# Exemplo de Pilha:
class No:
    def __init__(self, item):
        self.item = item
        self.contador = None  # Ponteiro para o próximo nó

class Pilha:
    def __init__(self):
        self.topo = None  # Armazena o topo da pilha

    def is_empty(self):
        """Verifica se a pilha está vazia."""
        return self.topo is None

    def push(self, item):
        """Adiciona um item no topo da pilha."""
        novo_no = No(item)  # Instancia um novo nó com o valor
        novo_no.contador = self.topo  # O próximo do novo nó é o topo atual
        self.topo = novo_no  # O topo da pilha agora é o novo nó

    def pop(self):
        """Remove e retorna o item do topo da pilha."""
        if self.is_empty():
            raise IndexError("pop de pilha vazia")
        
        item = self.topo.item  # O item que está no topo da pilha
        self.topo = self.topo.contador  # O topo agora é o próximo nó
        return item

    def peek(self):
        """Retorna o item do topo sem remover."""
        if self.is_empty():
            raise IndexError("topo de pilha vazia")
        return self.topo.item  # Retorna o item do topo da pilha

    def tamanho_pilha(self):
        """Retorna o número de elementos na pilha."""
        return self.tamanho


# Exemplo de uso:
pilha = Pilha()
pilha.push(10)
pilha.push(20)
pilha.push(30)

print(pilha.pop())  # Vai imprimir 30
print(pilha.peek())  # Vai imprimir 20
print(pilha.pop())  # Vai imprimir 20
print(pilha.pop())  # Vai imprimir 10
print(pilha.tamanho_pilha())  # Vai imprimir 2
