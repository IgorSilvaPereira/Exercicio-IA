import random


class EntradasValor():
    def __init__(self, valores, pesos):
        self.valor = int(valores)
        self.pesos = dict(pesos)


def somatorio(entradas, pesos):
    print(f'Peso do somatorio select = {pesos}')
    const = 0
    valorSom = 0
    for e in entradas:
        valorSom += e['valor'] * e['pesos'][pesos]
    return round(valorSom + const, 2)


def custo(ValorObt, ValorMelhor):
    return round(((ValorObt - ValorMelhor) ** 2), 2)


def gerar_pesos(QuantidadePesos):
    pesos = {}
    for n_peso in range(QuantidadePesos):
        pesos[f'w{n_peso}'] = round(random.random(), 2)
    return pesos


def gera_lista_entradas(qtd_entradas, PesoPEntr):
    entradas = []
    for n_entradas in range(qtd_entradas):
        vars()[f'e{str(n_entradas)}'] = {
            "nome": f'Entrada {str(n_entradas)}',
            "valor": round(random.random(), 2),
            "pesos": gerar_pesos(PesoPEntr)
        }
        entradas.append(vars()[f'e{str(n_entradas)}'])
    return entradas


def chamada_peso_randomico(entrada):
    return f'w{str(random.randint(0, len(entrada["pesos"]) - 1))}'


def chamada_peso_randomico(valor):
    return f'w{str(random.randint(0, int(valor) - 1))}'


def print_lista_entradas(entradas):
    for item in entradas:
        print(f'{item["nome"]}: valor = {item["valor"]}, pesos = {item["pesos"]} ')
    print('\n\n')


def print_lista_entradasB(entradas):
    for item in entradas:
        print(item)



def run():
    # variaveis de entradas e pesos
    qtd_entradas = 10
    QuantidadePesos = 10


    entradas = gera_lista_entradas(qtd_entradas, QuantidadePesos)
    print("\n")
    print_lista_entradas(entradas)

    somatorios = somatorio(entradas, chamada_peso_randomico(QuantidadePesos))

    print(f'Valor que Ativa a Função: {somatorios}')

    custos = custo(somatorios, 1)

    print(f'Valor de Custo da Função: {custos}')



if __name__ == '__main__':
    run()

