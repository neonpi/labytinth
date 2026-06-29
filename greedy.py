from entities import Maze, Node
from util import euclidian_distance, get_visited_dict


def greedy_search(maze: Maze) -> list[Node]:
    """Performs a greedy search for the maze's exit using the euclidian distance of each
    candidate node to the exit as the heuristic."""

    visited = get_visited_dict(maze)
    path: list[Node] = []
    stack = [maze.start()]

    while stack:
        node = stack.pop()
        if visited[node]:
            continue

        visited[node] = True
        path.append(node)

        neighbors = sorted(
            [n for n in node.edges], key=lambda n: euclidian_distance(n, maze.exit())
        )

        for neighbor in neighbors:
            if not visited[neighbor]:
                stack.append(neighbor)

    return path
