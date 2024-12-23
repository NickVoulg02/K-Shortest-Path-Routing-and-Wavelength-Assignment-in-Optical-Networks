import heapq


def dijkstra_k_shortest_paths(matrix, source, target, k):
    n = len(matrix)  # Number of nodes
    paths = []       # List to store k shortest paths
    heap = [(0, source - 1, [source])]  # Priority queue (cost, current_node, path_so_far)

    while heap and len(paths) < k:
        cost, node, path = heapq.heappop(heap)

        # If the path reaches the target, add it to the paths
        if node == target - 1:
            paths.append((cost, path))
            continue

        # Expand neighbors
        for neighbor in range(n):
            if matrix[node][neighbor] > 0 and (neighbor + 1) not in path:  # Check if a link exists and avoid loops
                new_cost = cost + matrix[node][neighbor]
                new_path = path + [neighbor + 1]  # Convert back to 1-based
                heapq.heappush(heap, (new_cost, neighbor, new_path))

    return paths


def find_all_k_shortest_paths(matrix, k):
    n = len(matrix)
    all_paths = {}  # Dictionary of all paths for each pair of nodes

    for source in range(1, n + 1):  # Iterate over all possible sources
        for target in range(source + 1, n + 1):  # Only consider targets greater than source to skip bidirectional edges
            paths = dijkstra_k_shortest_paths(matrix, source, target, k)
            all_paths[(source, target)] = paths

    return all_paths
