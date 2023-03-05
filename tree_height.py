import sys
import threading
import numpy as np

def compute_tree_height(n, prnts):
    chldrn = {i: [] for i in range(n)}
    root = []

    for i, parent in enumerate(prnts):
        if parent == -1:
            root.append(i)
        else:
            chldrn[parent].append(i)

    def find_max_depth(node, d):
        if not chldrn[node]:
            return d
        else:
            max_D = 0
            for child in chldrn[node]:
                child_D = find_max_depth(child, d+1)
                max_D = max(max_D, child_D)
            return max_D

    max_H = 0
    for r in root:
        treeheight = find_max_depth(r, 0)
        max_H = max(max_H, treeheight)

    return max_H + 1

def main():
    burts = input()

    if 'I' in burts:
        n = int(input())
        prnts = list(map(int, input().split()))
        print(compute_tree_height(n, prnts))

    elif 'F' in burts:
        fails = input()

        if 'a' in fails:
            return

        path = "test/" + fails
        with open(path, 'r') as v:
            n = int(v.readline())
            prnts = list(map(int, v.readline().split()))
            print(compute_tree_height(n, prnts))

sys.setrecursionlimit(10**7) 
threading.stack_size(2**27)
threading.Thread(target=main).start()
