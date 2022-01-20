from collections import deque
import sys

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BST:
    def __init__(self, root):
        self.root = root

    def insert(self, value):
        self.current_node = self.root
        while True:
            if value < self.current_node.value:
                if self.current_node.left != None:
                    self.current_node = self.current_node.left
                else:
                    self.current_node.left = Node(value)
                    break
            else:
                if self.current_node.right != None:
                    self.current_node = self.current_node.right
                else:
                    self.current_node.right = Node(value)
                    break

    def search(self, value):
        self.current_node = self.root
        while self.current_node:
            if self.current_node.value == value:
                return True
            elif self.current_node.value > value:
                self.current_node = self.current_node.left
            else:
                self.current_node = self.current_node.right
        return False
    
    def inorder_dequeue(self, queue):
        if (self.root):
            self.inorder_dequeue(self.root.left)
            queue.append_dequeue(self.root.value)
            self.inorder_dequeue(self.root.right)


def sum4each_position(n):
    if n < 10:
        return n
    return (n % 10) + sum4each_position(n//10)


def selfNum():
    ret = deque([])
    _curr = 1
    _bst = BST(Node(0))
    _result = 0
    sys.setrecursionlimit(10**6)
    while _result <= 100:
        _result = _curr + sum4each_position(_curr)
        _curr += 1
        if _bst.search(_result) == False:
            _bst.insert(_result)
    _bst.inorder_dequeue(ret)
    for i in range(100):
        if i == ret[0]:
            ret.pop()
            continue
        else:
            print(i)
    return ret

selfNum()
