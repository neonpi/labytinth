from entities import Maze, Node, is_exit
from stats import SearchStats
from util import distance, get_visited_dict, reconstruct_path


def greedy_search(maze: Maze) -> tuple[list[Node], SearchStats]:
    """Performs a greedy search for the maze's exit using the euclidian distance of each
    candidate node to the exit as the heuristic."""

    visited = get_visited_dict(maze)
    stack = [maze.start()]
    found = False
    parent: dict[Node, Node] = {}
    stats = SearchStats()

    while stack and not found:
        node = stack.pop()
        if visited[node]:
            continue

        visited[node] = True
        stats.nodes_expanded += 1

        if is_exit(maze, node):
            found = True
            continue

        for neighbor in node.edges:
            stats.nodes_visited += 1

        unvisited_neighbors = sorted(
            [n for n in node.edges if not visited[n]],
            key=lambda n: distance(n, maze.exit()),
            reverse=True,
        )

        for neighbor in unvisited_neighbors:
            parent[neighbor] = node
            stack.append(neighbor)

    return reconstruct_path(parent, maze.exit()), stats
