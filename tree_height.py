import sys
import threading
import numpy

class Node:
    def __init__(self, index):
        self.index = index
        self.children = []


def compute_height(n, parents):
    nodes = [Node(i) for i in range(n)]
    root = None
    for i in range(n):
        parent_index = parents[i]
        if parent_index == -1:
            root = nodes[i]
        else:
            nodes[parent_index].children.append(nodes[i])
    height = get_height(root)
    return height


def get_height(node):
    if not node.children:
        return 1
    max_child_height = 0
    for child in node.children:
        child_height = get_height(child)
        max_child_height = max(max_child_height, child_height)
    return max_child_height + 1


def main():
    n = int(input())
    parents = list(map(int, input().split()))

    height = compute_height(n, parents)
    print(height)

sys.setrecursionlimit(10*7)
threading.stack_size(2*27) 
threading.Thread(target=main).start()
