'''
numero = int(input("Digite um numero"))
divisores = 0
for divisor in range(1, numero):
    if numero % divisor == 0:
        divisores = divisores + 1
        if divisores > 1:
            break
if divisores > 1:
    print("não é primo")
else:
    print("é primo")
'''

'''
def indetificar_palindromo(texto):
    texto = texto.lower().replace(" ", "").replace(",", "").replace(".", "")
    invertido = texto [::-1]

    if texto == invertido:
        return True
    else:
        return False
    
entrada = input("Digite uma palavra, frase ou numero: ")
if indetificar_palindromo(entrada):
    print("A entrada é um palidromo")
else:
    print("A entrada não é um palindromo!")
'''
'''
def menu_inicial():
    print('Programa para Conversão de Temperaturas')
    print('1. Converter de Celsius para Fahrenheint')
    print('2. Converter de Fahrenhrint para Celsius')
def cel_fahr():
    C = float(input('Entre com a temperatura em graus Celsius'))
    F = C * (9 / 5) + 32
    print('Valor em Fahrenheit: {0}°F'.format(F))

def fahr_cel():
    F = float(input('Entre com a temperatura em graus Fahrenheit: '))
    C = (F - 32) * (5 / 9)
    print('Valor em Celsius: {0}°C'.format(C))

if __name__=='__main__':
    menu_inicial()
    escolha = input('Escolha o tipo de conversão que deseja realizar: ')

    if escolha == '1':
        cel_fahr()

    if escolha == '2':
        fahr_cel()
'''
'''
ano = int(input('Digite o ano: '))
if ano % 100 != 0 and ano % 4 == 0 or ano % 400 == 0:
    print("É um ano bissexto")
else:
    print("Não é um ano bissexto")
'''

valor = input('Digite um número menor que 20 que seja positivo: ')
if not valor.isdigit():
    print('Digite apenas números positivos!')
else:
    maximo = max(valor)
    minimo = min(valor)
    soma = 0
    media = soma
    for valor in valor: 
        soma += int(valor)
    print('O maior valor é:',maximo)
    print('O menor valor é:',minimo)
    print('A soma é:',soma)
    print('A média é:', media) 