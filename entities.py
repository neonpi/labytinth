from dataclasses import dataclass, field


@dataclass
class Node:
    """A node representing a walkable spot in the maze."""

    i: int
    j: int
    label: int
    edges: list["Node"] = field(default_factory=list["Node"])


def are_neighbors(node: Node, other: Node) -> bool:
    return abs(node.i - other.i) + abs(node.j - other.j) == 1


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


        
