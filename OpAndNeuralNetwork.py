entradas = [[0,0],[0,1],[1,0],[1,1]]
saidas = [0,1,1,1]
pesos = [0.0,0.0]
taxaDeAprendizagem = 0.1

def calculaSaida(entradas, pesos):
    s = 0
    for i in range(len(entradas)):
        s += entradas[i] * pesos[i]
    return stepFunction(s)

def stepFunction(soma):
    if (soma >=1):
        return 1
    return 0

def treinamento():
    erroTotal = 1
    while erroTotal != 0:
        erroTotal = 0
        for i in range(len(saidas)):
            valorSaida = calculaSaida(entradas[i], pesos)
            erro = saidas[i] - valorSaida
            erroTotal += erro
            for j in range(len(pesos)):
                pesos[j] = pesos[j] + (taxaDeAprendizagem * entradas[i][j] * erro)

treinamento()
print(f"Os pesos ajustados são: {pesos}")