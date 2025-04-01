import random
import os

# Função para limpar o terminal
def limpar_terminal() -> None:
    if os.name == 'nt':  # Windows
        os.system('cls')
    else:  # Unix/Linux/MacOS
        os.system('clear')

def adivinhacao() -> None:
    limpar_terminal()
    """
    Função principal do jogo de adivinhação de palavras.
    """
    lista_de_palavras_possiveis = ["computacao", "tecnologia", "cpu", "processador", "computador", "software", "aplicativo", "programa"]
    palavra_secreta = random.choice(lista_de_palavras_possiveis)
    tamanho_palavra = len(palavra_secreta)

    tentativas = 6
    letras_corretas = []
    letras_erradas = []

    while tentativas > 0:
        print(f"Tentativas restantes: {tentativas}")
        palavra_do_usuario = input(f"Digite o seu palpite para a palavra misteriosa ({tamanho_palavra} letras): \n").lower()

        if len(palavra_do_usuario) != tamanho_palavra:
            print(f"A palavra tem que ter {tamanho_palavra} letras!")
            continue

        dica = gerar_dica(palavra_secreta, palavra_do_usuario, letras_corretas, letras_erradas)
        print(f"Dica: {dica}")

        if palavra_do_usuario == palavra_secreta:
            print(f"Parabéns! Você acertou a palavra secreta: {palavra_secreta}")
            break

        for i, letra in enumerate(palavra_do_usuario):
            if letra == palavra_secreta[i]:
                if letra not in letras_corretas:
                    letras_corretas.append(letra)
            elif letra in palavra_secreta and letra not in letras_corretas:
                if letra not in letras_erradas:
                    letras_erradas.append(letra)

        tentativas -= 1

    if tentativas == 0:
        print(f"Suas tentativas acabaram. A palavra secreta era: {palavra_secreta}")

def gerar_dica(palavra_secreta, palavra_do_usuario, letras_corretas, letras_erradas):
    """
    Gera uma dica com base nas tentativas anteriores.

    Args:
        palavra_secreta: A palavra secreta a ser adivinhada.
        palavra_do_usuario: O palpite do usuário.
        letras_corretas: Lista de letras corretas na posição correta.
        letras_erradas: Lista de letras corretas, mas na posição errada.

    Returns:
        Uma string com a dica.
    """
    dica = ""
    for i, letra in enumerate(palavra_do_usuario):
        if letra == palavra_secreta[i]:
            dica += letra  
        elif letra in palavra_secreta:
            dica += "?" 
        else:
            dica += "_" 
    return dica

def main():
    limpar_terminal()
    print("\tBem-vindo ao jogo de adivinhação de palavras!")
    print("O tema é: Ciência da Computação.\nVamos lá!")
    
    while True:
        print("\n[1] Jogar")
        print("[2] Sair")
        
        escolha = input("Selecione uma opção: ")
        if escolha == "1":
            adivinhacao()
        elif escolha == "2":
            print("Obrigado por jogar!")
            break
        else:
            print("Escolha inválida, tente novamente.")

if __name__ == "__main__":
    main()
