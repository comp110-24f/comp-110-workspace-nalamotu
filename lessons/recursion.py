from __future__ import annotations


class Node:
    value: int
    next: Node | None

    def __init__(self, val: int, next: Node | None):
        self.value = val
        self.next = next


two: Node = Node(2, None)
one: Node = Node(1, two)


def sum(head: Node | None) -> int:
    """compute sum of values across all nodes in a linked list"""
    if head is None:
        return 0
    else:
        rest: int = sum(head.next)
        return head.value + rest


print(sum(one))
