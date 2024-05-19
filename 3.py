graph = {
    'Ada': {'Sabina':4, 'Lukas':1, 'Mark':9, 'John':7},
    'Gloria': {'Sabina':6, 'Vera':10, 'Mark':3},
    'Lukas': {'Sabina':1, 'Ada':1},
    'Sabina': {'Lukas':1, 'Vera':5, 'Ada':4, 'Gloria':6},
    'Vera': {'Sabina':5, 'John':7, 'Gloria':10, 'Randelon':8},
    'John': {'Vera':7, 'Mark':2, 'Marta':3, 'Randelon':9, 'Ada':7},
    'Mark': {'Gloria':3, 'Ada':9, 'John':2},
    'Marta': {'John':3, 'Randelon':4},
    'Randelon': {'John':9, 'Marta':4, 'Vera':8}
}

def dijkstra(graph, start):
    # Ініціалізація відстаней та множини невідвіданих вершин
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    unvisited = list(graph.keys())

    while unvisited:
        # Знаходження вершини з найменшою відстанню серед невідвіданих
        current_vertex = min(unvisited, key=lambda vertex: distances[vertex])

        # Якщо поточна відстань є нескінченністю, то ми завершили роботу
        if distances[current_vertex] == float('infinity'):
            break

        for neighbor, weight in graph[current_vertex].items():
            distance = distances[current_vertex] + weight

            # Якщо нова відстань коротша, то оновлюємо найкоротший шлях
            if distance < distances[neighbor]:
                distances[neighbor] = distance

        # Видаляємо поточну вершину з множини невідвіданих
        unvisited.remove(current_vertex)

    return distances

print(dijkstra(graph, 'Ada'))
