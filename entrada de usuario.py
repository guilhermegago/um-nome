def questao1(nome, idade, cidade):
    print("Nome:", nome, "- Idade:", idade, "- Cidade:", cidade + "!", sep=" ", end="\n")

def questao2():
   
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    operacao = input("Digite a operação desejada (+, -, *, /): ")

   
    if operacao == '+':
        resultado = num1 + num2
        print("Resultado:", resultado)
    elif operacao == '-':
        resultado = num1 - num2
        print("Resultado:", resultado)
    elif operacao == '*':
        resultado = num1 * num2
        print("Resultado:", resultado)
    elif operacao == '/':
        if num2 != 0:              resultado = num1 / num2
            print("Resultado:", resultado)
        else:
            print("Erro: Divisão por zero!")
    else:
        print("Operação inválida!")

def questao3():
   
    entrada = input("Digite os itens da lista de compras, separados por vírgula: ")
   
    itens = entrada.split(", ")
    
    for item in itens:
        print(item)

        
def quesao4():
    
    celsius = float(input("Digite a temperatura em graus Celsius: "))
   
    fahrenheit = (celsius * 9/5) + 32

    print("A temperatura em Fahrenheit é:", fahrenheit)

def questao5():
    nomes = [] 

    while True:
        nome = input("Digite um nome (ou 'sair' para encerrar): ")
        if nome.lower() == 'sair':
            break  
        nomes.append(nome)  

    for nome in nomes:
        print(nome)
