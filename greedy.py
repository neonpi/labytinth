from entities import Maze, Node, is_exit
from util import distance, get_visited_dict, reconstruct_path


def greedy_search(maze: Maze) -> list[Node]:
    """Performs a greedy search for the maze's exit using the euclidian distance of each
    candidate node to the exit as the heuristic."""

    visited = get_visited_dict(maze)
    stack = [maze.start()]
    found = False
    parent: dict[Node, Node] = {}

    while stack and not found:
        node = stack.pop()
        if visited[node]:
            continue

        visited[node] = True

        if is_exit(maze, node):
            found = True
            continue

        unvisited_neighbors = sorted(
            [n for n in node.edges if not visited[n]],
            key=lambda n: distance(n, maze.exit()),
            reverse=True,
        )

        for neighbor in unvisited_neighbors:
            parent[neighbor] = node
            stack.append(neighbor)

    return reconstruct_path(parent, maze.exit())
