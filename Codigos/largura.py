from collections import deque  # Importa a classe deque da biblioteca collections

def imprime_matriz(grafo):
    """Função para imprimir a matriz de adjacência."""
    print("Matriz de Adjacência:")
    for linha in grafo:
        print("  ".join(str(v) for v in linha))  # Imprime cada linha da matriz, separando os elementos por espaço
    print()

def busca_em_largura_passo_a_passo(grafo, inicio):
    """Função para realizar a busca em largura (BFS) passo a passo."""
    n = len(grafo)  # Obtém o número de vértices do grafo
    visitados = [False] * n  # Cria uma lista para marcar os vértices visitados, inicialmente todos como False
    fila = deque([inicio])  # Inicializa uma fila usando deque com o vértice inicial
    visitados[inicio] = True  # Marca o vértice inicial como visitado
    caminho = []  # Lista para armazenar o caminho percorrido

    while fila:  # Enquanto a fila não estiver vazia
        vertice = fila.popleft()  # Remove o primeiro elemento da fila
        caminho.append(vertice)  # Adiciona o vértice removido ao caminho percorrido
        
        print(f"Visitando vértice: A{vertice + 1}")  # Imprime o vértice atual
        imprime_matriz(grafo)  # Imprime a matriz de adjacência atualizada
        input("Pressione Enter para continuar...")  # Aguarda o usuário pressionar Enter para continuar
        
        for vizinho in range(n):  # Itera sobre os vizinhos do vértice atual
            # Se há uma conexão e o vizinho não foi visitado
            if grafo[vertice][vizinho] == 1 and not visitados[vizinho]:
                fila.append(vizinho)  # Adiciona o vizinho à fila
                visitados[vizinho] = True  # Marca o vizinho como visitado
                # Marca o vértice que visitou o vizinho na matriz de adjacência
                grafo[vertice][vizinho] = f"A{vertice + 1}"

    return caminho  # Retorna o caminho percorrido

# Matriz de adjacência fornecida
grafo = [
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

# Define o vértice inicial (A1, que corresponde ao índice 0)
vertice_inicial = 0

# Executa a busca em largura a partir do vértice inicial
caminho = busca_em_largura_passo_a_passo(grafo, vertice_inicial)

# Converte os índices no caminho para a nomenclatura A1, A2, ..., A10
caminho_nomenclatura = ["A" + str(vertice + 1) for vertice in caminho]

# Imprime o caminho percorrido pela busca em largura
print("Caminho percorrido pela busca em largura:", caminho_nomenclatura)
