def sequencia_valida(frase, dic):
    for i in frase:
        if (i == '('):
            dic['parenteses'] += 1

        elif (i == ')' and dic['parenteses'] > 0):
            dic['parenteses'] -= 1
        
        elif (i == ')' and dic['parenteses'] < 1):
            dic['parenteses'] = None
            break
        
        elif (i == '[' and dic['parenteses'] < 1):
            dic['colchetes'] += 1
        
        elif (i == ']' and dic['colchetes'] > 0 and dic['parenteses'] < 1):
            dic['colchetes'] -= 1 
        
        elif (i == ']' and dic['colchetes'] < 1):
            dic['colchetes'] = None
            break
        
        elif (i == '{' and dic['parenteses'] < 1 and dic['colchetes'] < 1):
            dic['chaves'] += 1
        
        elif (i == '}' and dic['chaves'] > 0 and dic['parenteses'] < 1 and dic['colchetes'] < 1):
            dic['chaves'] -= 1 
        
        elif (i == '}' and dic['chaves'] < 1):
            dic['chaves'] = None
            break
        
        else:
            break
            
frase = input("digite uma sring de brackets: ")
d = {"parenteses":0, "colchetes": 0, "chaves":0}
sequencia_valida(frase, d)
if (d['parenteses'] == 0 and d['colchetes'] == 0 and d['chaves'] == 0):
    print("sequencia válida")
else:
    print('sequencia inválida')