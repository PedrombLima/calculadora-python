def somar(x, y):
    return x + y

def subtrair(x, y):
    return x - y

def multiplicar(x, y):
    return x * y

def dividir(x, y):
    if y == 0:
        return "Erro! Divisão por zero"
    return x / y

print("Selecionar a operação")
print("1 - Somar")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

escolha = input("Digite sua escolha (1/2/3/4): ")

num1 = float(input("Digite o primeiro numero: "))
num2 = float(input("Digite o segundo numero: "))

if escolha == '1':
    print(f"{num1} + {num2} = {somar(num1, num2)}")
elif escolha == '2':
    print(f"{num1} - {num2} = {subtrair(num1, num2)}")
elif escolha == '3':
    print(f"{num1} * {num2} = {multiplicar(num1, num2)}")
elif escolha =='4':
    print(f"{num1} / {num2} = {dividir(num1, num2)}")
else:
    print("Opção inválida!")