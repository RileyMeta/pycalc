from dataclasses import dataclass

@dataclass
class NumberNode:
    value: float

    def __repr__(self):
        return f"{self.value}"

@dataclass
class AddNode:
    node_a: any
    node_b: any

    def __repr__(self):
        return f"({self.node_a}+{self.node_b})"

@dataclass
class SubNode:
    node_a: any
    node_b: any

    def __repr__(self):
        return f"({self.node_a}-{self.node_b})"

@dataclass
class MultiplyNode:
    node_a: any
    node_b: any

    def __repr__(self):
        return f"({self.node_a}*{self.node_b})"

@dataclass
class DivideNode:
    node_a: any
    node_b: any

    def __repr__(self):
        return f"({self.node_a}/{self.node_b})"

@dataclass
class PositiveNode:
    node: any

    def __repr__(self):
        return f"(+{self.node})"

@dataclass
class NegativeNode:
    node: any

    def __repr__(self):
        return f"(-{self.node})"