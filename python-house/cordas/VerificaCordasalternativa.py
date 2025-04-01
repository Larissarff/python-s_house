#alternativa de função para verificar as cordas

def neutralise(s1, s2):
    result = ""
    for i in range(len(s1)):
        if s1[i] == s2[i]:
            result += s1[i]
        else:
            result += "0"
    return result
    
