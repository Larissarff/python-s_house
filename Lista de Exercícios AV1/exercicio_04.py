import random
from typing import List, Optional

class Usuario:
    def __init__(self, nome: str, senha: str, deposito_inicial: float) -> None:
        self.nome : str = nome
        self.senha : str = senha
        self.deposito : float = deposito_inicial
        self.numero_conta : str = self.gerar_numero_conta()

    def gerar_numero_conta(self) -> str:
        return str(random.randint(100000, 999999))

    def __str__(self) -> str:
        return f"Nome: {self.nome}, Número da Conta: {self.numero_conta}, Saldo: R${self.deposito:.2f}"
    
contas : List[Usuario] = []

def cadastrarConta() -> None:
    nome: str = input("Digite o nome do representante da conta: ")
    senha: str = input("Digite a senha da conta: ")
    deposito_inicial: float = float(input("Digite o depósito inicial (0 ou mais): "))

    nova_conta: Usuario = Usuario(nome, senha, deposito_inicial)
    
    contas.append(nova_conta)

    print(f"Conta cadastrada com sucesso! {nova_conta}")

def acessarAConta() -> None:

    options : int = int(input("Selecione: \n [1] - Realizar um depósito \n [2] - Realizar um saque \n [3] - Realizar uma transferência \n [4] - Emitir extrato da conta \n [5] - Voltar ao menu \n"))

    

    match options:
        case 1:
            return deposito()
        case 2:
            return saque()
        case 3:
            return transferencia()
        case 4:
            return extrato()
        case 5:
            return main()
        case _:
            exit 

    def deposito() -> None:
        erros : int = 0

        while True:
            conta_desejada : str = input("Digite o nome do representante da conta que deseja fazer o depósito:  ")  

            if conta_desejada == "0":
                print("Saindo da função de depósito...")
                return

            for conta in contas:
                if conta.nome == conta_desejada:

                    deposito_valor: float = float(input("Conta encontrada! Insira o valor que deseja depositar: "))

                    if deposito_valor > 0:

                        senha_digitada : str = input("Digite sua senha da conta:  ")

                        if erros < 3:

                            if conta.senha == senha_digitada:

                                conta.deposito += deposito_valor  
                                print(f"Depósito de R${deposito_valor:.2f} realizado com sucesso! Novo saldo: R${conta.deposito:.2f}")
                            else:

                                print("Senha digitada incorretamente! Tente novamente, com 3 tentativas erradas, sua senha será bloqueada!\n")
                                erros = erros + 1
                        else:
                            print("Sua senha foi bloqueada! Deve ir ao caixa eletrônico para desbloquea-la!  ")
                    else:
                        print("O valor do depósito deve ser positivo.")
                    return
                
            print("Conta não encontrada. Verifique o nome e tente novamente.")



    def saque() -> None:

        erros : int = 0

        while True:
            conta_desejada : str = input("Digite o nome do representante da conta que deseja fazer o saque:  ")  

            if conta_desejada == "0":
                print("Saindo da função de saque...")
                return

            for conta in contas:
                if conta.nome == conta_desejada:

                    saque_valor: float = float(input("Conta encontrada! Insira o valor que deseja sacar: "))

                    if saque_valor > 0:

                        senha_digitada : str = input("Digite sua senha da conta:  ")
                        if erros < 3:

                            if conta.senha == senha_digitada:
                                conta.deposito += saque_valor  
                                print(f"Saque de R${saque_valor:.2f} realizado com sucesso! Novo saldo: R${conta.deposito:.2f}")
                            else:
                                print("Senha digitada incorretamente! Tente novamente, com 3 tentativas erradas, sua senha será bloqueada!\n")
                                erros = erros + 1
                        else:
                            print("Sua senha foi bloqueada! Deve ir ao caixa eletrônico para desbloquea-la!  ")

                    else:
                        print("O valor do saque deve ser positivo.")
                    return
            print("Conta não encontrada. Verifique o nome e tente novamente.")

    def transferencia() -> None:
        print(" SUA TRANSFERENCIA")

    def extrato() -> None:
        print(" SUA TRANSFERENCIA")
        

def main() -> None:
    while True:
        print("\tBem vindo ao banco!")
        escolha : int = int(input("Selecione: \n [1] - Cadastrar nova conta \n [2] - Realizar Operações na conta \n"))

        match escolha:
            case 1:
                return cadastrarConta()
            case 2:
                return acessarAConta()
            case _:
                return "Valor de escolha inválido"
if __name__ == "__main__":
    main()
