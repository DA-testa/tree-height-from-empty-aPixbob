# python3

import sys
import threading
import numpy
import sys

class Node:
    def __init__(self):
        self.parent = None
        self.children = []

def build_tree(n, parents):
    # Create nodes
    nodes = [Node() for i in range(n)]
    
    # Build tree
    for i in range(n):
        parent = parents[i]
        if parent == -1:
            root = nodes[i]
        else:
            nodes[parent].children.append(nodes[i])
            nodes[i].parent = nodes[parent]
    
    return root

def compute_height(root):
    # Base case: leaf node
    if not root.children:
        return 0
    
    # Recursive case: find maximum depth of children
    max_depth = 0
    for child in root.children:
        max_depth = max(max_depth, compute_height(child))
    
    return max_depth + 1

def main():
    # Read input
    n = int(input())
    parents = list(map(int, input().split()))
    
    # Build tree
    root = build_tree(n, parents)
    
    # Compute and output height
    print(compute_height(root))

if __name__ == '__main__':
    sys.setrecursionlimit(10**7)
    main()
