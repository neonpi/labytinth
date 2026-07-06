from collections import deque

from entities import Maze, Node, is_exit
from stats import SearchStats
from util import get_visited_dict, reconstruct_path


def breadth_first_search(maze: Maze) -> tuple[list[Node], SearchStats]:
    visited = get_visited_dict(maze)
    queue = deque([maze.start()])
    parent: dict[Node, Node] = {}
    stats = SearchStats()

    while queue:
        node = queue.popleft()

        if visited[node]:
            continue

        visited[node] = True
        stats.nodes_expanded += 1

        if is_exit(maze, node):
            break

        for neighbor in node.edges:
            stats.nodes_visited += 1
            if not visited[neighbor]:
                parent[neighbor] = node
                queue.append(neighbor)

    return reconstruct_path(parent, maze.exit()), stats
