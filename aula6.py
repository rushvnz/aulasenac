'''
def fatorial(a):
    if a == 0:
        return 1
    else: 
        fat = 1
        for i in range (1, a+1):
             fat *= i
        return fat

a = int(input("digite seu numero: "))
print("O fatorial de", a , " é: ", fatorial (a))
'''

'''
idade = int(input("Digite sua idade:"))


altura = float(input("Digite sua altura:"))


nome = input("digite seu nome:")


tem_carro = input("Tem carro? (Sim/Não):")

tem_carro = tem_carro.lower() == "sim"

print("Idade: ", idade)
print("Altura: ", altura)
print("nome: ", nome)
print("Tem carro? ","Sim" if tem_carro else "Não")
'''
'''
def contagem_regressiva():
    numero = int(input("Digite um numero inteiro positivo: "))

    if numero <= 0:
        print("Por favor digite um numero inteiro positivo.")
        contagem_regressiva()

    else:
        while numero >= 0:
            print(numero)
            numero -= 1

contagem_regressiva()
'''

'''
def soma (a , b):
    return a + b
def subtracao(a, b):
    return a - b
def multiplicacao(a,b):
    return a * b
def divisao(a,b):
    if b != 0:
        return a / b
    else:
        return "Divisao nao permitida"
    

def calculadora():
    print("Bem-vindo a calculadora em python!")
    print("Selecione a opcao desejada:")
    print("1: soma")
    print("2: Subtração")
    print("3: Multiplicação")
    print("4: divisão")

    escolha = input("Digite sua escolha 1/2/3/4: ")
    if escolha in ('1', '2', '3', '4'):
        num1 = float(input("Digite o primeiro numero:"))
        num2 = float(input("Digite o segundo numero:"))

        if escolha == '1':
            print("resultado", soma(num1,num2))
        elif escolha == '2':
            print("resultado", subtracao(num1,num2))
        elif escolha == '3':
            print("resultado", multiplicacao(num1,num2))
        elif escolha == '4':
            print("resultado", divisao(num1,num2))
        
    else:
        print("Escolha invalida")

calculadora()
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
    