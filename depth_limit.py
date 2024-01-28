def depth_limited_search(graph, start, goal, depth_limit):
    visited = set()

    def dls(node, depth):
        if depth > depth_limit:
            return False  # Reached depth limit, stop further exploration beyond this depth

        print(node, " ", end="")
        visited.add(node)

        if node == goal:
            return True  

        for neighbour in graph[node]:
            if neighbour not in visited:
                if dls(neighbour, depth + 1):
                    return True 

        return False 

    print("Depth-Limited Search with depth limit", depth_limit, ":")
    if not dls(start, 0):
        print("Goal not found within the depth limit.")

graph = {'A': ['B', 'C'],
         'B': ['D', 'E'],
         'C': ['F', 'G'],
         'D': [],
         'E': ['H', 'I'],
         'F': [],
         'G': ['J'],
         'H': [],
         'I': [],
         'J': []}

depth_limited_search(graph,'A','J',3)
