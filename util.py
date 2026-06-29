from entities import Maze, Node


def get_visited_dict(maze: Maze) -> dict[Node, bool]:
    """Returns a dict with all nodes mapped to false, signaling that none have been visited yet."""
    nodes = {}
    for node in maze.nodes:
        nodes[node] = False

    return nodes


def distance(source: Node, destination: Node) -> float:
    x_delta = destination.x - source.x
    y_delta = destination.y - source.y
    return (x_delta**2 - y_delta**2) ** (1 / 2)
