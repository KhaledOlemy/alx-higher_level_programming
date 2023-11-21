#!/usr/bin/python3
"""class Node"""


class Node:
    """Node declaration"""
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


"""class SinglyLinkedList"""


class SinglyLinkedList:
    """SinglyLinkedList declaration"""
    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        new_node = Node(value)
        if self.__head is None:
            self.__head = new_node
            new_node.next_node = None
        elif self.__head.data > value:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            holder = self.__head
            while holder:
                if holder.next_node:
                    if holder.data <= value and holder.next_node.data >= value:
                        new_node.next_node = holder.next_node
                        holder.next_node = new_node
                        break
                else:
                    new_node.next_node = None
                    holder.next_node = new_node
                    break
                holder = holder.next_node

    def __str__(self):
        nums = []
        holder = self.__head
        while holder:
            nums.append(str(holder.data))
            holder = holder.next_node
        nums = "\n".join(nums)
        return nums
