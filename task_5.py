from collections import deque
import heapq
import uuid

import networkx as nx
import matplotlib.pyplot as plt

from task_4 import Node, draw_tree, heap_to_tree_max, heap_to_tree_min


def main():
    heap = [3,7,10,15,8,22,37,53,42,11]

    root = heap_to_tree_min(heap)
    bfs(root)
    draw_tree(root)

    root = heap_to_tree_max(heap)
    dfs(root)
    draw_tree(root)


def dfs(root: Node, start_color="#12098D"):
    if root == None:
        return
    
    stack = [root]
    color = start_color

    while stack:
        node = stack.pop()
        node.color = color

        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

        color = lighten_hex(color, 0.15)


def bfs(root: Node, start_color="#862406"):
    if root == None:
        return
    
    queue = deque()
    queue.append(root)
    color = start_color

    while queue:
        node = queue.popleft()
        node.color = color

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

        color = lighten_hex(color, 0.15)


def lighten_hex(hex_color: str, k: float) -> str:
    hex_color = hex_color.lstrip("#")

    r = int(hex_color[0:2], 16)
    g = int(hex_color[2:4], 16)
    b = int(hex_color[4:6], 16)

    r = int(r + (255 - r) * k)
    g = int(g + (255 - g) * k)
    b = int(b + (255 - b) * k)

    return f"#{r:02X}{g:02X}{b:02X}"



if __name__ == "__main__":
    main()
