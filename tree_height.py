import sys
import threading
import numpy

def compute_height(n, parents):
    children = {i: [] for i in range(n)}
    roots = []

    for i, parent in enumerate(parents):
        if parent == -1:
            roots.append(i)
        else:
            children[parent].append(i)

    def find_max_depth(node, depth):
        if not children[node]:
            return depth
        else:
            max_depth = 0
            for child in children[node]:
                child_depth = find_max_depth(child, depth+1)
                max_depth = max(max_depth, child_depth)
            return max_depth

    max_height = 0
    for root in roots:
        height = find_max_depth(root, 0)
        max_height = max(max_height, height)

    return max_height + 1


def main():
    letter = input()

    if 'I' in letter:
        n = int(input())
        parents = list(map(int, input().split()))
        print(compute_height(n, parents))

    elif 'F' in letter:
        file_name = input()

        if 'a' in file_name:
            return

        file_path = "test/" + file_name
        with open(file_path, 'r') as f:
            n = int(f.readline())
            parents = list(map(int, f.readline().split()))
            print(compute_height(n, parents))


sys.setrecursionlimit(10**7) 
threading.stack_size(2**27)
threading.Thread(target=main).start()
