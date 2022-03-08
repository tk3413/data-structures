"""
description: sort implementations

author: Taimore Khan
"""
import math
from typing import Optional, List

class Sort:
    def builtin_sort(self, unordered_list: List) -> List:
        return sorted(unordered_list)

    def merge_sort(self, unordered_list: List) -> List:
        if len(unordered_list) == 1:
            return unordered_list
        else:
            # divide
            divided_list: (List, List) = self.divide_list(unordered_list)
            left: List = self.merge_sort(divided_list[0])
            right: List = self.merge_sort(divided_list[1])

            # merge
            left_iterator: int = 0
            right_iterator: int = 0

            sorted_list: List = []
            sorted_iterator: int = 0

            while left_iterator < len(left) and right_iterator <len(right):
                if left[left_iterator] < right[right_iterator]:
                    sorted_list.append(left[left_iterator])
                    left_iterator += 1
                elif left[left_iterator] >= right[right_iterator]:
                    sorted_list.append(right[right_iterator])
                    right_iterator += 1

            while left_iterator < len(left):
                sorted_list.append(left[left_iterator])
                left_iterator += 1

            while right_iterator < len(right):
                sorted_list.append(right[right_iterator])
                right_iterator += 1

        return sorted_list

    def get_middle(self, l: List) -> int:
        return math.floor(len(l)/2)

    def divide_list(self, l: List) -> (List, List):
        middle: int = self.get_middle(l)
        return (l[:middle], l[middle:])
