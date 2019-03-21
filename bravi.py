def sequencia_valida(frase, dic):
    for i in frase:
        if (i == '(' and not dic['parenteses']):
            dic['parenteses'] = True
        elif (i == ')' and dic['parenteses']):
            dic['parenteses'] = False
        elif (i == '[' and not dic['colchetes']):
            dic['colchetes'] = True
        elif (i == ']' and dic['colchetes']):
            dic['colchetes'] = False
        elif (i == '{' and not dic['chaves']):
            dic['chaves'] = True
        elif (i == '}' and dic['chaves']):
            dic['chaves'] = False
        else:
            break
            
frase = input("digite uma sring de brackets: ")
d = {"parenteses":False, "colchetes": False, "chaves":False}
sequencia_valida(frase, d)
if (not d['parenteses'] and not d['colchetes'] and not d['chaves']):
    print("sequencia válida")
else:
    print('sequencia inválida ')