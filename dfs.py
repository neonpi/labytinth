from entities import Maze, Node, is_exit
from stats import SearchStats
from util import get_visited_dict, reconstruct_path


def depth_limited_search(maze: Maze) -> tuple[list[Node], SearchStats]:
    depth_limit = len(maze.nodes)
    visited = get_visited_dict(maze)
    stack: list[tuple[Node, int]] = [(maze.start(), 0)]
    parent: dict[Node, Node] = {}
    stats = SearchStats()

    while stack:
        node, depth = stack.pop()

        if visited[node]:
            continue

        visited[node] = True
        stats.nodes_expanded += 1

        if is_exit(maze, node):
            break

        if depth < depth_limit:
            for neighbor in node.edges:
                stats.nodes_visited += 1
                if not visited[neighbor]:
                    parent[neighbor] = node
                    stack.append((neighbor, depth + 1))

    return reconstruct_path(parent, maze.exit()), stats
