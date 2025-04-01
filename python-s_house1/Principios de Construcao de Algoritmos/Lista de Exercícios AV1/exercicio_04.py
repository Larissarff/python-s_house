import random
import os
from typing import List, Optional

class Usuario:
    def __init__(self, nome: str, senha: str, deposito_inicial: float) -> None:
        self.nome: str = nome
        self.senha: str = senha
        self.deposito: float = deposito_inicial
        self.numero_conta: str = self.gerar_numero_conta()
        self.extrato: List[str] = []

    def gerar_numero_conta(self) -> str:
        return str(random.randint(100000, 999999))

    def __str__(self) -> str:
        return f"Nome: {self.nome}, Número da Conta: {self.numero_conta}, Saldo: R${self.deposito:.2f}"

contas: List[Usuario] = []

# Função para limpar o terminal
def limpar_terminal() -> None:
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:  # Unix/Linux/MacOS
        os.system('clear')

# Função para verificar a senha
def verificar_senha(conta: Usuario) -> bool:
    if not conta.habilitada:
        print("Sua conta está bloqueada! Vá ao caixa eletrônico para desbloqueá-la.")
        return False

    limpar_terminal()
    erros: int = 0
    while erros < 3:
        senha_digitada = input("Digite sua senha da conta: ")
        if conta.senha == senha_digitada:
            return True
        else:
            print("Senha incorreta! Tente novamente.")
            erros += 1

    print("Sua senha foi bloqueada após 3 tentativas! Vá ao caixa eletrônico para desbloqueá-la.")
    conta.habilitada = False
    return False

def cadastrarConta() -> None:
    limpar_terminal()
    nome: str = input("Digite o nome do representante da conta: ")
    senha: str = input("Digite a senha da conta: ")
    deposito_inicial: float = float(input("Digite o depósito inicial (0 ou mais): "))

    nova_conta: Usuario = Usuario(nome, senha, deposito_inicial)
    contas.append(nova_conta)

    print(f"Conta cadastrada com sucesso! {nova_conta}\n"
          f"Clique em \"Enter\" para voltar para o menu \n")


def acessarAConta() -> None:
    limpar_terminal()
    numero_conta: str = input("Digite o número da sua conta: ")

    conta = next((conta for conta in contas if conta.numero_conta == numero_conta), None)
    
    if conta is None:
        print("Conta não encontrada.")
        return

    if verificar_senha(conta):
        if not conta.habilitada:
            print("Conta bloqueada. Vá ao caixa eletrônico para desbloqueá-la.")
            return
        
        options: int = int(input("Selecione:\n"
                                 f"[1] - Realizar um depósito\n"
                                 f"[2] - Realizar um saque\n"
                                 f"[3] - Realizar uma transferência\n"
                                 f"[4] - Emitir extrato da conta\n"
                                 f"[5] - Voltar ao menu \n"))
        match options:
            case 1:
                deposito()
            case 2:
                saque()
            case 3:
                transferencia()
            case 4:
                extrato()
            case 5:
                main()
            case _:
                exit()
    else:
        print("Acesso negado.")


def deposito() -> None:
    limpar_terminal()
    conta_desejada = input("Digite o nome do representante da conta que deseja fazer o depósito: ")

    for conta in contas:
        if conta.nome == conta_desejada:
            deposito_valor: float = float(input("Conta encontrada! Insira o valor que deseja depositar: "))
            if deposito_valor > 0:
                if verificar_senha(conta):
                    conta.deposito += deposito_valor
                    conta.extrato.append(f"Depósito de R${deposito_valor:.2f}")
                    print(f"Depósito de R${deposito_valor:.2f} realizado com sucesso! Novo saldo: R${conta.deposito:.2f}")
            else:
                print("O valor do depósito deve ser positivo.")
            return
    print("Conta não encontrada. Verifique o nome e tente novamente.")

def saque() -> None:
    limpar_terminal()
    conta_desejada = input("Digite o nome do representante da conta que deseja fazer o saque: ")

    for conta in contas:
        if conta.nome == conta_desejada:
            saque_valor: float = float(input("Conta encontrada! Insira o valor que deseja sacar: "))
            if saque_valor > 0 and saque_valor <= conta.deposito:
                if verificar_senha(conta):
                    conta.deposito -= saque_valor
                    conta.extrato.append(f"Saque de R${saque_valor:.2f}")
                    print(f"Saque de R${saque_valor:.2f} realizado com sucesso! Novo saldo: R${conta.deposito:.2f}")
            else:
                print("O valor do saque deve ser positivo ou menor que o saldo.")
            return
    print("Conta não encontrada. Verifique o nome e tente novamente.")

def transferencia() -> None:
    limpar_terminal()
    conta_origem = input("Digite o nome do representante da conta de origem: ")
    conta_destino = input("Digite o nome do representante da conta de destino: ")

    for conta_o in contas:
        if conta_o.nome == conta_origem:
            for conta_d in contas:
                if conta_d.nome == conta_destino:
                    valor: float = float(input("Insira o valor a ser transferido: "))
                    if valor > 0 and valor <= conta_o.deposito:
                        if verificar_senha(conta_o):
                            conta_o.deposito -= valor
                            conta_d.deposito += valor
                            conta_o.extrato.append(f"Transferência de R${valor:.2f} para a conta {conta_d.numero_conta}")
                            conta_d.extrato.append(f"Transferência de R${valor:.2f} da conta {conta_o.numero_conta}")
                            print(f"Transferência de R${valor:.2f} realizada com sucesso!")
                    else:
                        print("Saldo insuficiente ou valor inválido.")
                    return
            print("Conta de destino não encontrada.")
            return
    print("Conta de origem não encontrada.")

def extrato() -> None:
    limpar_terminal()
    conta_desejada = input("Digite o nome do representante da conta que deseja emitir o extrato: ")

    for conta in contas:
        if conta.nome == conta_desejada:
            print(f"Extrato da conta {conta.numero_conta}:")
            for transacao in conta.extrato:
                print(transacao)
            print(f"Saldo atual: R${conta.deposito:.2f}")
            return
    print("Conta não encontrada.")

def main() -> None:
    limpar_terminal()
    while True:
        print("\tBem-vindo ao banco!")
        escolha = input("Selecione: \n [1] - Cadastrar nova conta \n [2] - Realizar Operações na conta \n")
        
        # Verifica se o valor está vazio ou fora do esperado
        if escolha == "":
            limpar_terminal()
            print("Você pressionou Enter sem selecionar uma opção válida. Por favor, escolha uma opção válida.")
            continue
        
        try:
            escolha_int = int(escolha)
            match escolha_int:
                case 1:
                    cadastrarConta()
                case 2:
                    acessarAConta()
                case _:
                    print("Valor de escolha inválido. Por favor, escolha entre as opções 1 ou 2.")
        except ValueError:
            limpar_terminal()
            print("Entrada inválida. Por favor, escolha entre as opções 1 ou 2.")

if __name__ == "__main__":
    main()
