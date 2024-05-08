def questao1():
    
    nome = input("Digite seu nome: ")

    nome_arquivo = "nome_usuario.txt"
    with open(nome_arquivo, "w") as arquivo:
        arquivo.write(nome)
        print("Nome gravado com sucesso no arquivo '{}'.".format(nome_arquivo))


def questao2():
   
    nome_arquivo = input("Digite o nome do arquivo de texto: ")
    
    with open(nome_arquivo, "r") as arquivo:
        conteudo = arquivo.read()
        print("Conteúdo do arquivo '{}':".format(nome_arquivo))
        print(conteudo)


def questao3(origem, destino):
   
    with open(origem, "r") as arquivo_origem:
        conteudo = arquivo_origem.read()

    
    with open(destino, "w") as arquivo_destino:
        arquivo_destino.write(conteudo)

    print("Conteúdo do arquivo '{}' copiado para o arquivo '{}' com sucesso.".format(origem, destino))

def questao4(numero, arquivo):
    try:
        
        with open(arquivo, "r") as f:
            
            for linha in f:
               
                partes = linha.split(",")
                                if partes[0].strip() == str(numero):
                    print("Nome correspondente ao número {}: {}".format(numero, partes[1].strip()))
                    return
            
            print("Não foi encontrado nenhum nome correspondente ao número {}.".format(numero))
    except FileNotFoundError:
        print("Arquivo não encontrado.")
