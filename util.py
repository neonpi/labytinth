from entities import Maze, Node
from stats import SearchStats


def print_constructed_path(path: list[Node]):
    path_string = "A"

    for node in path[1:-1]:
        path_string += " -> " + str(node)

    path_string += " -> B"
    print(path_string)


def print_search_result(path: list[Node], stats: SearchStats, elapsed_time: float):
    """Prints every property required by the spec for a single search method's result."""
    depth = len(path) - 1  # every edge has unit cost, so depth equals cost

    print_constructed_path(path)
    print(f"Custo/Profundidade: {depth}")
    print(f"Nós expandidos: {stats.nodes_expanded}")
    print(f"Nós visitados: {stats.nodes_visited}")
    print(f"Fator de ramificação médio: {stats.branching_factor():.2f}")
    print(f"Tempo de execução: {elapsed_time:.6f}s")


def get_visited_dict(maze: Maze) -> dict[Node, bool]:
    """Returns a dict with all nodes mapped to false, signaling that none have been visited yet."""
    nodes: dict[Node, bool] = {}
    for node in maze.nodes:
        nodes[node] = False

    return nodes


def distance(source: Node, destination: Node) -> int:
    """Returns the Manhattan distance between the two given nodes"""
    x_delta = source.x - destination.x
    y_delta = source.y - destination.y
    return abs(x_delta) + abs(y_delta)


def reconstruct_path(parent: dict[Node, Node], exit: Node) -> list[Node]:
    """Reconstructs the path built during the search using each node's set parent"""
    path: list[Node] = []
    node = exit

    while node in parent.keys():
        path.append(node)
        node = parent[node]

    path.append(node)
    path.reverse()
    return path
