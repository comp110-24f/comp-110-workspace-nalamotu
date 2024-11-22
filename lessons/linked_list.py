from __future__ import annotations


class Node:
    value: int
    next: Node | None

    def __init__(self, value: int, next: Node | None):
        self.value = value
        self.next = next

    def __str__(self) -> str:
        """Represent a Node object as a string"""
        rest: str = "?"
        if self.next is None:
            rest = "None"
        else:
            rest = str(self.next)
        return f"{self.value} -> {rest}"


three: Node = Node(3, None)
two: Node = Node(2, three)
one: Node = Node(1, two)
courses: Node = Node(110, Node(210, Node(301, None)))


def to_str(head: Node | None) -> str:
    """Represent a linked list as a str"""
    if head is None:
        return "None"
    else:
        rest: str = to_str(head.next)
        return f"{head.value} -> {rest}"


def last(head: Node) -> int:
    """Return the last value of a linked list"""
    if head.next is None:
        return head.value
    else:
        last_elem: int = last(head.next)
        return last_elem


def value_at(head: Node | None, index: int) -> int:
    """Find the value of a linked list at a particular index."""
    if head is None:
        raise IndexError("Index is out of bounds on the list.")
    if index == 0:
        return head.value

    return value_at(head.next, index - 1)


def max(head: Node | None) -> int:
    """Find the maximum value in the linked list."""
    if head is None:
        raise ValueError("Cannot call max with None")
    if head.next is None:
        return head.value
    max_in_rest = max(head.next)
    if head.value > max_in_rest:
        return head.value
    else:
        return max_in_rest


def r_range(start: int, end: int) -> Node | None:
    if start == end:
        return None
    else:
        return Node(start, r_range(start + 1, end))


print(to_str(r_range(3, 7)))
