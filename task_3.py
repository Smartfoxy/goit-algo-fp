import heapq
import networkx as nx
import matplotlib.pyplot as plt


def main():
    city_graph = create_graph(get_stops(), get_roads())
    distances, prev = dijkstra_heap(city_graph, "Park")

    print_final(distances)
    print_paths(prev, "Park")

    show_graph(city_graph)


def create_graph(stops, roads_with_weights):
    G = nx.Graph()
    G.add_nodes_from(stops)

    for u, v, w in roads_with_weights:
        G.add_edge(u, v, weight=w)

    return G


def dijkstra_heap(graph: nx.Graph, start):
    distances = {vertex: float('inf') for vertex in graph.nodes()}
    distances[start] = 0
    prev = {v: None for v in graph.nodes()}

    d_heap = [(0, start)]
    visited = set()

    while d_heap:
        current_dist, u = heapq.heappop(d_heap)

        if u in visited:
            continue
        visited.add(u)

        for v, attrs in graph[u].items():
            w = attrs.get("weight", 1)
            new_dist = current_dist + w
            if new_dist < distances[v]:
                distances[v] = new_dist
                prev[v] = u
                heapq.heappush(d_heap, (new_dist, v))

        print_table(distances, visited)

    return distances, prev


def get_stops():
    return [
        "City Center",
        "Train Station",
        "University",
        "Shopping Mall",
        "Residential Area",
        "Park",
        "Hospital",
        "Old Town"
    ]


def get_roads():
    return[
        ("City Center", "Train Station", 4),
        ("City Center", "University", 3),
        ("Train Station", "University", 5),

        ("University", "Park", 2),
        ("Park", "Residential Area", 7),
        ("Residential Area", "University", 5),

        ("City Center", "Shopping Mall", 3),
        ("Shopping Mall", "Residential Area", 6),
        ("Shopping Mall", "Old Town", 1),
        ("Old Town", "City Center", 2),

        ("Hospital", "University", 2),
        ("Hospital", "Residential Area", 4)
    ]


def print_table(distances, visited):
    print("{:<10} {:<10} {:<10}".format("Вершина", "Відстань", "Перевірено"))
    print("-" * 30)
    
    for vertex in distances:
        distance = distances[vertex]
        if distance == float('inf'):
            distance = "∞"
        else:
            distance = str(distance)
        
        status = "Так" if vertex in visited else "Ні"
        print("{:<15} {:<10} {:<10}".format(vertex, distance, status))
    print("\n")


def reconstruct_path(prev, start, end):
    path = []
    cur = end
    while cur is not None:
        path.append(cur)
        cur = prev[cur]
    path.reverse()

    return path if path and path[0] == start else []


def print_paths(prev, start):
    print("\nНайкоротші шляхи від вершини:", start)
    for v in prev:
        if v == start:
            continue
        path = reconstruct_path(prev, start, v)
        if path:
            print(" → ".join(path))
        else:
            print(f"{v}: шлях не знайдено")


def print_final(distances):
    print("\nФінальні найкоротші відстані:")
    for v, d in distances.items():
        d_str = "∞" if d == float("inf") else str(d)
        print(f"- {v}: {d_str}")


def show_graph(graph: nx.Graph):
    plt.figure(figsize=(10, 8))
    plt.title("Transportation Network of a Small City", color="blue")

    pos = nx.spring_layout(graph, seed=42)
    nx.draw(graph, pos, with_labels=True, node_size=1500, node_color="lightblue", font_size=10,
        font_color="blue")
    plt.show()


if __name__ == "__main__":
    main()
