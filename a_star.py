from entities import Maze, Node, is_exit
from util import distance, reconstruct_path


def a_star_search(maze: Maze) -> list[Node]:
    """Performs the A* search of start to exit of the given maze returning the path constructed
    during the process"""
    open: list[Node] = []
    closed: list[Node] = []
    parent: dict[Node, Node] = {}
    g_evaluation: dict[Node, int] = {}
    h_evaluation: dict[Node, int] = {}
    f_evaluation: dict[Node, int] = {}

    open.append(maze.start())
    g_evaluation[maze.start()] = 0
    h_evaluation[maze.start()] = distance(maze.start(), maze.exit())
    f_evaluation[maze.start()] = g_evaluation[maze.start()] + h_evaluation[maze.start()]

    while open:
        node = min(open, key=lambda n: f_evaluation[n])
        open.remove(node)

        if is_exit(maze, node):
            break

        for neighbor in node.edges:
            if neighbor in closed:
                continue

            temp_g = g_evaluation[node] + 1  # we're not using weighted edges

            if neighbor not in open:
                open.append(neighbor)
            elif temp_g >= g_evaluation[neighbor]:
                continue  # worse path than the one to be explored later

            parent[neighbor] = node
            g_evaluation[neighbor] = temp_g
            h_evaluation[neighbor] = distance(neighbor, maze.exit())
            f_evaluation[neighbor] = g_evaluation[neighbor] + h_evaluation[neighbor]

        closed.append(node)

    return reconstruct_path(parent, maze.exit())
