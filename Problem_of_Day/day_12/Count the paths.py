def count_paths(V, edges, src, dest):
    # Build adjacency list manually
    graph = [[] for _ in range(V)]
    for u, v in edges:
        graph[u].append(v)

    # Memoization dictionary
    memo = {}

    def dfs(node):
        if node == dest:
            return 1
        if node in memo:
            return memo[node]

        total_paths = 0
        for neighbor in graph[node]:
            total_paths += dfs(neighbor)

        memo[node] = total_paths
        return total_paths

    return dfs(src)

edges = [[0,1], [0,3], [2,0], [2,1], [1,3]]
V = 4
src = 2
dest = 3
print(count_paths(V, edges, src, dest))  # Output: 3

edges = [[0,1], [1,2], [1,3], [2,3]]
V = 4
src = 0
dest = 3
print(count_paths(V, edges, src, dest))  # Output: 2
