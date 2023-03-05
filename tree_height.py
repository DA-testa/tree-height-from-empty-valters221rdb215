import sys
import threading
import numpy

def compute_height(n, parents):
    children = {i: [] for i in range(n)}
    
    for i in range(n):
        parent = parents[i]
        if parent != -1:
            children[parent].append(i)
    
    def get_height(node):
        if children[node] == []:
            return 1
        else:
            heights = [get_height(child) for child in children[node]]
            return max(heights) + 1
    
    root = parents.index(-1)
    height = get_height(root)
    
    return height

def main():
    n = int(input())
    parents = list(map(int, input().split()))
    
    height = compute_height(n, parents)
    
    print(height)

if __name__ == '__main__':
    sys.setrecursionlimit(10**7)
    threading.stack_size(2**27)
    
    thread = threading.Thread(target=main)
    thread.start()
    thread.join()
