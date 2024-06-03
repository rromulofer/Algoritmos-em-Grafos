def busca_em_largura(grafo, inicio):
    visitados = [False] * len(grafo)
    fila = [inicio]
    visitados[inicio] = True
    caminho = []

    while fila:
        vertice = fila.pop(0)
        caminho.append(vertice)
        for vizinho in range(len(grafo)):
            if grafo[vertice][vizinho] == 1 and not visitados[vizinho]:
                fila.append(vizinho)
                visitados[vizinho] = True

    return caminho

# Matriz de adjacência fornecida
grafo = [
    # A1 A2 A3 A4 A5 A6 A7 A8 A9 A10
    [ 0, 1, 1, 0, 0, 0, 0, 0, 0, 0],  # A1
    [ 1, 0, 0, 1, 1, 0, 0, 0, 0, 0],  # A2
    [ 1, 0, 0, 1, 0, 1, 0, 0, 0, 0],  # A3
    [ 0, 1, 1, 0, 1, 1, 0, 0, 0, 0],  # A4
    [ 0, 1, 0, 1, 0, 0, 1, 1, 0, 0],  # A5
    [ 0, 0, 1, 1, 0, 0, 1, 0, 1, 0],  # A6
    [ 0, 0, 0, 0, 1, 1, 0, 1, 1, 0],  # A7
    [ 0, 0, 0, 0, 1, 0, 1, 0, 0, 1],  # A8
    [ 0, 0, 0, 0, 0, 1, 1, 0, 0, 1],  # A9
    [ 0, 0, 0, 0, 0, 0, 0, 1, 1, 0]   # A10
]

vertice_inicial = 0  # Começa a busca no vértice A1 (índice 0)
caminho = busca_em_largura(grafo, vertice_inicial)

# Converte os índices para a nomenclatura A1, A2, ..., A10
caminho_nomenclatura = ["A" + str(vertice + 1) for vertice in caminho]

print("Caminho percorrido pela busca em largura:", caminho_nomenclatura)
