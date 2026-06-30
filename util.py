from entities import Maze, Node


def print_constructed_path(path: list[Node]):
    path_string = "A"

    for node in path[1:-1]:
        path_string += " -> " + str(node)

    path_string += " -> B"
    print(path_string)


def get_visited_dict(maze: Maze) -> dict[Node, bool]:
    """Returns a dict with all nodes mapped to false, signaling that none have been visited yet."""
    nodes: dict[Node, bool] = {}
    for node in maze.nodes:
        nodes[node] = False

    return nodes


def distance(source: Node, destination: Node) -> float:
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
