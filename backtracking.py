from entities import Maze, Node, is_exit
from util import get_visited_dict, reconstruct_path


def _dfs(
    node: Node, parent: dict[Node, Node], visited: dict[Node, bool], maze: Maze
) -> bool:
    visited[node] = True

    if is_exit(maze, node):
        return True

    for neighbor in node.edges:
        if not visited[neighbor]:
            parent[neighbor] = node
            if _dfs(neighbor, parent, visited, maze):
                return True

    return False


def backtracking_search(maze: Maze) -> list[Node]:
    visited = get_visited_dict(maze)
    parent: dict[Node, Node] = {}

    _dfs(maze.start(), parent, visited, maze)
    return reconstruct_path(parent, maze.exit())
