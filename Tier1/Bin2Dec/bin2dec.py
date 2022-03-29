from cgi import print_form
import re

i = 0
binario  = ""
while i < 8:
    digitado = str(input("Digite um numero binaria: "))
    result = re.search(r'[^0,1]|[0,1]{2,}',digitado)
    if(result):
        print('Caracter incorreto')
        quit()
    binario += digitado
    i+=1
    
tamanho_string = len(binario)
soma = 0
zero = 0
potencia = tamanho_string -1
calculo = 0
while zero < tamanho_string:
    
    digito  = int(binario[zero])
    
    calculo += int(digito * (2**potencia))
    zero+=1
    potencia -=1
    
print('resultado em decimal: '+str(calculo))
