import sys
import matplotlib.pyplot as plt
import networkx as nx

V = 6  # Número de vértices

def select_min_vertex(value, processed):
    minimum = sys.maxsize
    vertex = -1
    for i in range(V):
        if not processed[i] and value[i] < minimum:
            vertex = i
            minimum = value[i]
    return vertex

def dijkstra(graph):
    parent = [-1] * V  # Almacena la estructura del camino más corto
    value = [sys.maxsize] * V  # Valores iniciales de las distancias
    processed = [False] * V  # TRUE si el vértice ya está procesado

    # Nodo inicial
    value[0] = 0  # La distancia al nodo inicial es 0

    for _ in range(V - 1):
        # Seleccionar el mejor vértice usando un método greedy
        u = select_min_vertex(value, processed)
        processed[u] = True

        # Relajar los vértices adyacentes
        for j in range(V):
            # Condiciones de relajación:
            # 1. Hay una arista entre u y j
            # 2. El vértice j no ha sido procesado
            # 3. La nueva distancia es menor que la distancia actual
            if graph[u][j] != 0 and not processed[j] and value[u] != sys.maxsize and (value[u] + graph[u][j] < value[j]):
                value[j] = value[u] + graph[u][j]
                parent[j] = u

    # Imprimir el grafo del camino más corto
    edges = []
    for i in range(1, V):
        print(f"U->V: {parent[i]}->{i}  wt = {graph[parent[i]][i]}")
        edges.append((parent[i], i, graph[parent[i]][i]))  # Guardar las aristas del camino más corto
    
    # Generar gráfica
    plot_graph(graph, edges)

def plot_graph(graph, edges):
    G = nx.Graph()
    # Añadir nodos
    for i in range(V):
        G.add_node(i)
    
    # Añadir todas las aristas con sus pesos
    for i in range(V):
        for j in range(V):
            if graph[i][j] != 0:
                G.add_edge(i, j, weight=graph[i][j])

    # Posiciones para los nodos
    pos = nx.spring_layout(G)

    # Dibujar todos los nodos y aristas
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=10)
    nx.draw_networkx_edge_labels(G, pos, edge_labels={(i, j): graph[i][j] for i in range(V) for j in range(V) if graph[i][j] != 0})

    # Resaltar el camino más corto
    nx.draw_networkx_edges(G, pos, edgelist=[(u, v) for u, v, w in edges], edge_color='red', width=2)

    # Mostrar la gráfica
    plt.title("Camino más corto usando Dijkstra")
    plt.show()

# Grafo de entrada
graph = [
    [0, 1, 4, 0, 0, 0],
    [1, 0, 4, 2, 7, 0],
    [4, 4, 0, 3, 5, 0],
    [0, 2, 3, 0, 4, 6],
    [0, 7, 5, 4, 0, 7],
    [0, 0, 0, 6, 7, 0]
]

# Llamada a la función Dijkstra
dijkstra(graph)
