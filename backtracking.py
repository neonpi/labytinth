from entities import Maze, Node, is_exit
from stats import SearchStats
from util import get_visited_dict, reconstruct_path


def _dfs(
    node: Node,
    parent: dict[Node, Node],
    visited: dict[Node, bool],
    maze: Maze,
    stats: SearchStats,
) -> bool:
    visited[node] = True
    stats.nodes_expanded += 1

    if is_exit(maze, node):
        return True

    for neighbor in node.edges:
        stats.nodes_visited += 1
        if not visited[neighbor]:
            parent[neighbor] = node
            if _dfs(neighbor, parent, visited, maze, stats):
                return True

    return False


def backtracking_search(maze: Maze) -> tuple[list[Node], SearchStats]:
    visited = get_visited_dict(maze)
    parent: dict[Node, Node] = {}
    stats = SearchStats()

    _dfs(maze.start(), parent, visited, maze, stats)
    return reconstruct_path(parent, maze.exit()), stats
