import sys
import dns.resolver


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
    args = sys.argv  # leitura dos argumentos
    try:
        dominio = args[1]
        arquivo = args[2]
    except:
        print("Problema ao tentar ler os argumentos!\nExemplo de uso: python dnsbrute.py site.com wordlists.txt")
        exit()

    lista = carregarWordList(arquivo)
    subdominio = montarSubDominio(lista, dominio)
    for sub in subdominio:
        try:
            respostas = dns.resolver.query(sub, "a")
        except:
            pass
        for resultado in respostas:
            print(sub, resultado)
except Exception as e:
    print("Ocorreu algum problema. Erro: ", e)
