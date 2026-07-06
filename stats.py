from dataclasses import dataclass


@dataclass
class SearchStats:
    """Tracks statistics gathered during a search."""

    nodes_expanded: int = 0
    nodes_visited: int = 0

    def branching_factor(self) -> float:
        """Average branching factor: nodes visited per node expanded."""
        if self.nodes_expanded == 0:
            return 0.0
        return self.nodes_visited / self.nodes_expanded
