def calcular_soma_media(lista):
    """
    Calcula a soma e a média de uma lista de números.

    Args:
    lista (list): Uma lista de números.

    Returns:
    tuple: Uma tupla contendo a soma e a média dos números na lista.
    """
    soma = sum(lista)
    media = soma / len(lista)
    return soma, media

def substituir_palavra(lista, palavra_antiga, palavra_nova):
    """
    Substitui todas as ocorrências de uma palavra por outra em uma lista de palavras.

    Args:
    lista (list): Uma lista de palavras.
    palavra_antiga (str): A palavra a ser substituída.
    palavra_nova (str): A nova palavra que substituirá a palavra antiga.

    Returns:
    list: A lista com as palavras substituídas.
    """
    return [palavra_nova if palavra == palavra_antiga else palavra for palavra in lista]

def gerar_triangulo(num_linhas):
    """
    Gera um triângulo de asteriscos para o número de linhas informado.

    Args:
    num_linhas (int): O número de linhas do triângulo.

    Returns:
    None
    """
    for i in range(1, num_linhas + 1):
        print('*' * i)

# Teste das funções
if __name__ == "__main__":
    # Testando função calcular_soma_media
    lista_numeros = [1, 2, 3, 4]
    soma, media = calcular_soma_media(lista_numeros)
    print("Soma:", soma)
    print("Média:", media)

    # Testando função substituir_palavra
    lista_palavras = ["fluzão", "botafogo", "gremio", "fluzão"]
    palavra_antiga = "fluzão"
    palavra_nova = "vasco"
    nova_lista = substituir_palavra(lista_palavras, palavra_antiga, palavra_nova)
    print("Lista alterada:", nova_lista)

    # Testando função gerar_triangulo
    num_linhas = 4
    print("Triângulo de asteriscos:")
    gerar_triangulo(num_linhas)
