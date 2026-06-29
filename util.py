from entities import Maze, Node


def print_constructed_path(path: list[Node]):
    path_string = "A "

    for node in path[1:-1]:
        path_string += " -> " + str(node)
    
    path_string += "-> B"
    print(path_string)


def get_visited_dict(maze: Maze) -> dict[Node, bool]:
    """Returns a dict with all nodes mapped to false, signaling that none have been visited yet."""
    nodes: dict[Node, bool] = {}
    for node in maze.nodes:
        nodes[node] = False

    return nodes


def euclidian_distance(source: Node, destination: Node) -> float:
    x_delta = destination.x - source.x
    y_delta = destination.y - source.y
    return (x_delta**2 + y_delta**2) ** (1 / 2)
