#TESTES E ESTUDOS

def main() -> None:

    if __name__ == "__main__": #Esta linha verifica se o script está sendo executado diretamente pelo Python ou se está sendo importado como um módulo em outro script.
        main()

# '__name__:' É uma variável especial em Python que é definida pelo interpretador.

#__name__: É uma variável especial em Python que é definida pelo interpretador. Quando um script Python é executado diretamente, o valor de __name__ é "__main__".
# No entanto, se o script for importado como um módulo em outro script, o valor de __name__ será o nome do módulo (o nome do arquivo sem a extensão .py).
# exemplo:
# outro_script.py
import script

# O uso da variável __name__ permite que você escreva código que só deve ser executado quando o script é o programa principal.
