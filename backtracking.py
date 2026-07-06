from collections.abc import Iterator

from entities import Maze, Node, is_exit
from stats import SearchStats
from util import get_visited_dict, reconstruct_path


def backtracking_search(maze: Maze) -> tuple[list[Node], SearchStats]:
    visited = get_visited_dict(maze)
    parent: dict[Node, Node] = {}
    stats = SearchStats()

    start = maze.start()
    visited[start] = True
    stats.nodes_expanded += 1

    if is_exit(maze, start):
        return reconstruct_path(parent, maze.exit()), stats

    stack: list[tuple[Node, Iterator[Node]]] = [(start, iter(start.edges))]
    while stack:
        node, edges = stack[-1]
        descended = False

        for neighbor in edges:
            stats.nodes_visited += 1
            if visited[neighbor]:
                continue

            parent[neighbor] = node
            visited[neighbor] = True
            stats.nodes_expanded += 1

            if is_exit(maze, neighbor):
                return reconstruct_path(parent, maze.exit()), stats

            stack.append((neighbor, iter(neighbor.edges)))
            descended = True
            break

        if not descended:
            stack.pop()

    return reconstruct_path(parent, maze.exit()), stats
