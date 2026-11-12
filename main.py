from collections import deque

# ---------------------------------------------------------
# PART 1: BINARY TREE  (SESTUAL)
#               S
#             /   \
#           E       S'
#          / \     / \
#         T   U   A   L
# ---------------------------------------------------------
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def build_tree():
    root = Node("S")
    root.left = Node("E")
    root.right = Node("S'")
    root.left.left = Node("T")
    root.left.right = Node("U")
    root.right.left = Node("A")
    root.right.right = Node("L")
    return root


def tree_bfs(root):
    """Breadth-First Search using a queue (level order)."""
    result = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        result.append(node.data)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return result


def tree_dfs(node, result=None):
    """Depth-First Search using recursion (preorder: root, left, right)."""
    if result is None:
        result = []
    if node is None:
        return result
    result.append(node.data)
    tree_dfs(node.left, result)
    tree_dfs(node.right, result)
    return result


# ---------------------------------------------------------
# PART 2: GRAPH  (SESTUAL)
#   L --- A --- S1 --- E --- S2
#               |             |
#               T ----------- U
# ---------------------------------------------------------
graph = {
    "S1": ["E", "T", "A"],
    "E":  ["S1", "S2"],
    "S2": ["E", "U"],
    "T":  ["S1", "U"],
    "U":  ["T", "S2"],
    "A":  ["S1", "L"],
    "L":  ["A"],
}


def graph_bfs(graph, start):
    """Breadth-First Search using a queue and a visited set."""
    visited = {start}
    queue = deque([start])
    result = []
    while queue:
        vertex = queue.popleft()
        result.append(vertex)
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return result


def graph_dfs(graph, vertex, visited=None, result=None):
    """Depth-First Search using recursion and a visited set."""
    if visited is None:
        visited = set()
    if result is None:
        result = []
    visited.add(vertex)
    result.append(vertex)
    for neighbor in graph[vertex]:
        if neighbor not in visited:
            graph_dfs(graph, neighbor, visited, result)
    return result


# ---------------------------------------------------------
# MAIN
# ---------------------------------------------------------
if __name__ == "__main__":
    root = build_tree()
    print("BINARY TREE")
    print("BFS:", " - ".join(tree_bfs(root)))
    print("DFS:", " - ".join(tree_dfs(root)))

    print("\nGRAPH (start at S1)")
    print("BFS:", " - ".join(graph_bfs(graph, "S1")))
    print("DFS:", " - ".join(graph_dfs(graph, "S1")))