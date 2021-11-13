"""
description: classic stack implementation in python

author: Taimore Khan
"""


class Stack:
    def __init__(self):
        self.size = 0
        self.items = []
        self.type = None

    def get_size(self) -> int:
        return self.size

    def get_type(self) -> any:
        return self.type

    def push(self, item: any) -> None:
        self._validate_type(item)
        self.items.append(item)
        self.size += 1

    def _validate_type(self, item: any) -> None:
        if self.size == 0:
            self.type = type(item)
        if type(item) is not self.type:
            raise TypeError("only one type permitted in this stack")

    def peek(self) -> any:
        if self.size > 0:
            return self.items[self.size - 1]
        else:
            return None

    def pop(self) -> any:
        if self.size >= 1:
            self.size -= 1
            if self.size == 0:
                self.type = None
            return self.items.pop()
        else:
            return None
