"""Linked List Utility Functions."""

from __future__ import annotations

__author__: str = "730766272"


class Node:
    """A Node class."""

    value: int
    next: Node | None

    def __init__(self, value: int, next: Node | None):
        """Initializing value of the Node and next element."""
        self.value = value
        self.next = next

    def __str__(self) -> str:
        """Represent a Node object as a string."""
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
    """Represent a linked list as a str."""
    if head is None:
        return "None"
    else:
        rest: str = to_str(head.next)
        return f"{head.value} -> {rest}"


def last(head: Node) -> int:
    """Return the last value of a linked list."""
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


def linkify(items: list[int]) -> Node | None:
    """Return a linked list with values matching items in the list."""
    if items == []:
        return None
    return Node(items[0], linkify(items[1:]))


def scale(head: Node | None, factor: int) -> Node | None:
    """Multiply a linked list by a scale factor and return the output."""
    if head is None:
        return None
    return Node(head.value * factor, scale(head.next, factor))


print(scale(linkify([1, 2, 3]), 2))
