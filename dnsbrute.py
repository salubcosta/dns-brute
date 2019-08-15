import sys
import dns.resolver

args = sys.argv  # leitura dos argumentos


# Carrega arquivo e retorna uma lista de strings
def carregarWordList(arquivo):
    try:
        return open(arquivo).read().splitlines()  # retorna uma lista de strings
    except Exception as e:
        print("Erro ao carregar o arquivo. Erro: ", e)
        return []


def montarSubDominio(linhas, site):
    subdominio = []
    for linha in linhas:
        subdominio.append(linha + '.' + site)
    return subdominio

try:
    dominio = args[1]
    arquivo = args[2]
    lista = carregarWordList(arquivo)
    subdomain = montarSubDominio(lista, dominio)
    for item in subdomain:
        respostas = dns.resolver.query(item, "a")
        for resultado in respostas:
            print(item, resultado)
except Exception as e:
    print("Ocorreu algum problema. Erro: ", e)