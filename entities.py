from dataclasses import dataclass, field


@dataclass
class Node:
    """A node representing a walkable spot in the maze."""

    y: int
    x: int
    label: int
    edges: list["Node"] = field(default_factory=list["Node"])


def are_neighbors(node: Node, other: Node) -> bool:
    return abs(node.y - other.y) + abs(node.x - other.x) == 1


@dataclass
class Maze:
    """Maze represented as a graph with its recorded dimensions."""

    width: int
    height: int
    nodes: list[Node]

    def __init__(self, width: int, height: int, nodes: list[Node]):
        self.width = width
        self.height = height
        self.nodes = nodes

        for i, node in enumerate(self.nodes):
            for other in self.nodes[i:]:
                if are_neighbors(node, other):
                    node.edges.append(other)
                    other.edges.append(node)


def is_start(maze: Maze, node: Node) -> bool:
    """Checks if the node is the start of the given maze"""
    return maze.nodes.index(node) == 0


def is_end(maze: Maze, node: Node) -> bool:
    """Checks if the node is the end of the given maze"""
    return maze.nodes.index(node) == len(maze.nodes) - 1
