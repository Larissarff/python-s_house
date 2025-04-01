# Dado duas cordas compostas de +E a -, devolvê-la que mostra como as duas cadeias interagem da seguinte maneira:

#    Quando os positivos e positivos interagem, eles permanecem positivos.
#    Quando negativos e negativos interagem, eles permanecem negativos.
#    Mas quando os negativos e positivos interagem, eles se tornam neutros e são mostrados como o número. 0- A . (í a , , , , , í , .

# Exemplo de trabalho

# ("+-+", "+--") ➞ "+-0"
# Compare the first characters of each string, then the next in turn.
# "+" against a "+" returns another "+".
# "-" against a "-" returns another "-".
# "+" against a "-" returns "0".


#Código:

def interacao_cordas(corda1, corda2):
    resultado = ""
    
    # Verifica se as cordas têm o mesmo comprimento
    if len(corda1) != len(corda2):  #len = conta a quantidade de argumentos na string
        raise ValueError("As cordas devem ter o mesmo comprimento.") 
    
    # Percorre as strings buscando as semelhanças
    for c1, c2 in zip(corda1, corda2): # 
        if c1 == '+' and c2 == '+':
            resultado += '+'
        elif c1 == '-' and c2 == '-':
            resultado += '-'
        else:
            resultado += '0'
    
    return resultado

def verificaTam(texto):
    if len(texto) == 0:
        raise ValueError("A string está vazia. Digite uma sequência válida.")

def main():
    try:
        tam = int(input("Digite o tamanho das cordas: \n"))
        
        corda1 = input("Digite sua primeira corda: \n")
        verificaTam(corda1)
        if len(corda1) != tam:  # Verifica novamente sobre o tamanho
            raise ValueError("A primeira corda não tem o comprimento especificado.")
        
        corda2 = input("Digite sua segunda corda: \n")
        verificaTam(corda2)
        if len(corda2) != tam:  # Verifica novamente sobre o tamanho
            raise ValueError("A segunda corda não tem o comprimento especificado.")
        
        print("A corda resultante é: ")
        print(interacao_cordas(corda1, corda2))
    
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
