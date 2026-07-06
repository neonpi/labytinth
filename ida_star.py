from entities import Maze, Node, is_exit
from stats import SearchStats
from util import distance, reconstruct_path

INF = 10**9  # large enough integer to use as threshold


def _dfs(
    maze: Maze,
    node: Node,
    parent: dict[Node, Node],
    g: int,
    threshold: int,
    stats: SearchStats,
    best_g: dict[Node, int],
) -> tuple[bool, int]:
    """DFS search used in IDA*.

    Parameters:
    * maze - where to perform the search
    * node - root node for this search
    * parent - dict mapping each node to its parent
    * g - cost from root to current node
    * threshold - IDA*'s current threshold value
    * stats - stats accumulator, mutated across recursive calls and iterations
    * best_g - best (lowest) g seen for each node during this iteration, used to
      avoid re-exploring a node through an equal-or-worse path (grid mazes have
      many cycles/alternate paths, so ancestor-only cycle checks blow up)

    Return - if no goal was found, returns
    """
    f = g + distance(node, maze.exit())

    if f > threshold:
        return (False, f)

    stats.nodes_expanded += 1
    best_g[node] = g

    if is_exit(maze, node):
        return (True, threshold)

    min_exceeded = INF

    for neighbor in node.edges:
        stats.nodes_visited += 1
        if neighbor in parent:
            continue

        neighbor_g = g + 1
        if neighbor in best_g and best_g[neighbor] <= neighbor_g:
            continue

        parent[neighbor] = node
        found, new_threshold = _dfs(maze, neighbor, parent, neighbor_g, threshold, stats, best_g)

        if found:
            return (True, threshold)

        del parent[neighbor]

        if new_threshold < min_exceeded:
            min_exceeded = new_threshold

    return (False, min_exceeded)


def ida_star_search(maze: Maze) -> tuple[list[Node], SearchStats]:
    """Performs an IDA* search for the maze's exit"""
    threshold = distance(maze.start(), maze.exit())
    parent: dict[Node, Node] = {}
    found: bool = False
    stats = SearchStats()

    while not found:
        parent.clear()
        best_g: dict[Node, int] = {}
        found, new_threshold = _dfs(maze, maze.start(), parent, 0, threshold, stats, best_g)

        if found:
            continue

        if new_threshold == INF:  # didn't find a node
            return [], stats

        threshold = new_threshold

    return reconstruct_path(parent, maze.exit()), stats
