from entities import Maze, Node, is_exit
from util import distance, reconstruct_path

INF = 10**9  # large enough integer to use as threshold


def _dfs(
    maze: Maze, node: Node, parent: dict[Node, Node], g: int, threshold: int
) -> tuple[bool, int]:
    """DFS search used in IDA*.

    Parameters:
    * maze - where to perform the search
    * node - root node for this search
    * parent - dict mapping each node to its parent
    * g - cost from root to current node
    * threshold - IDA*'s current threshold value

    Return - if no goal was found, returns
    """
    f = g + distance(node, maze.exit())

    if f > threshold:
        return (False, f)

    if is_exit(maze, node):
        return (True, threshold)

    min_exceeded = INF

    for neighbor in node.edges:
        if neighbor in parent:
            continue

        parent[neighbor] = node
        found, new_threshold = _dfs(maze, neighbor, parent, g + 1, threshold)

        if found:
            return (True, threshold)

        del parent[neighbor]

        if new_threshold < min_exceeded:
            min_exceeded = new_threshold

    return (False, min_exceeded)


def ida_star_search(maze: Maze) -> list[Node]:
    """Performs an IDA* search for the maze's exit"""
    threshold = distance(maze.start(), maze.exit())
    parent: dict[Node, Node] = {}
    found: bool = False

    while not found:
        parent.clear()
        found, new_threshold = _dfs(maze, maze.start(), parent, 0, threshold)

        if found:
            continue

        if new_threshold == INF:  # didn't find a node
            return []

        threshold = new_threshold

    return reconstruct_path(parent, maze.exit())
