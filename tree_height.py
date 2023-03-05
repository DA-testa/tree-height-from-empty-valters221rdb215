import sys
import threading
import numpy

def compute_height(num_nodes, parents):
    tree = numpy.zeros(num_nodes)

    def get_height(node):
        if tree[node] != 0:
            return tree[node]

        if parents[node] == -1:
            tree[node] = 1
        else:
            tree[node] = 1 + get_height(parents[node])

        return tree[node]

    for node in range(num_nodes):
        get_height(node)

    return int(max(tree))


def main():
    file_name = input().strip()

    while 'a' in file_name or 'A' in file_name:
        file_name = input().strip()

    try:
        with open(f"./{file_name}") as file:
            num_nodes = int(file.readline().strip())
            parents = list(map(int, file.readline().split()))

        result = compute_height(num_nodes, parents)

        with open(f"./{file_name.split('.')[0]}_output.txt", 'w') as file:
            file.write(str(result))

    except FileNotFoundError:
        pass


sys.setrecursionlimit(10**7)
threading.stack_size(2**27)

threading.Thread(target=main).start()
