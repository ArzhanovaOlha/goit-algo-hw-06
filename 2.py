from collections import deque

graph = {
    'Ada': ['Sabina', 'Lukas', 'Mark', 'John'],
    'Gloria': ['Sabina', 'Vera', 'Mark'],
    'Lukas': ['Sabina', 'Ada'],
    'Sabina': ['Lukas', 'Vera', 'Ada', 'Gloria'],
    'Vera': ['Sabina', 'John', 'Gloria', 'Randelon'],
    'John': ['Vera', 'Mark', 'Marta', 'Randelon', 'Ada'],
    'Mark': ['Gloria', 'Ada', 'John'],
    'Marta': ['John', 'Randelon'],
    'Randelon': ['John', 'Marta', 'Vera']
}

def dfs_iterative(graph, start_vertex):
    visited = set()
    count = 0
    # Використовуємо стек для зберігання вершин
    stack = [start_vertex]
    while stack:
        count +=1
        # Вилучаємо вершину зі стеку
        vertex = stack.pop()
        if vertex not in visited:

            print(vertex, end=' ')
            # Відвідуємо вершину
            visited.add(vertex)
            # Додаємо сусідні вершини до стеку
            stack.extend(reversed(graph[vertex]))
    print(f'DFS алгоритм використовується для виявлення повного шляху. Довжина шляху для алгоритма DFS: {count}')



def bfs_iterative(graph, start):
    # Ініціалізація порожньої множини для зберігання відвіданих вершин
    visited = set()
    # Ініціалізація черги з початковою вершиною
    queue = deque([start])
    count = 0
    while queue:  # Поки черга не порожня, продовжуємо обхід
        # Вилучаємо першу вершину з черги
        count +=1
        vertex = queue.popleft()
        # Перевіряємо, чи була вершина відвідана раніше
        if vertex not in visited:
            # Якщо не була відвідана, друкуємо її
            print(vertex, end=" ")
            # Додаємо вершину до множини відвіданих вершин
            visited.add(vertex)
            # Додаємо всіх невідвіданих сусідів вершини до кінця черги
            # Операція різниці множин вилучає вже відвідані вершини зі списку сусідів
            queue.extend(set(graph[vertex]) - visited)
    # Повертаємо множину відвіданих вершин після завершення обходу
    return print(f'BFS алгоритм забезпечує знаходження найкоротшого маршруту. Довжина шляху для алгоритма BFS: {count}')



dfs_iterative(graph, 'Ada')
bfs_iterative(graph, 'Ada')