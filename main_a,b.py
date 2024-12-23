import dijkstra_shortest_path
import path_analysis


if __name__ == "__main__":
    # Define adjacency matrix
    matrix = [
        [0, 0, 5, 0, 0],
        [0, 0, 0, 3, 7],
        [5, 0, 0, 1, 0],
        [0, 3, 1, 0, 1],
        [0, 7, 0, 1, 0]
    ]

    k = 3  # Number of shortest paths to find for each pair

    # Find all k shortest paths
    all_k_shortest_paths = dijkstra_shortest_path.find_all_k_shortest_paths(matrix, k)

    # Create initial graph
    initial_graph = path_analysis.create_graph(matrix)
    path_analysis.plot_graph(initial_graph, "Initial Topology")

    print("All k shortest paths (skipping bidirectional edges):")
    for (source, target), paths in all_k_shortest_paths.items():
        print(f"From {source} to {target}:")
        for i, (cost, path) in enumerate(paths, 1):
            print(f"  {i}: Cost = {cost}, Path = {path}")

    # Analyze paths
    selected_paths, edge_counts, max_app, min_app, avg_app = path_analysis.analyze_paths(all_k_shortest_paths)

    print("Selected paths with the least edges:")
    for (source, target), path in selected_paths.items():
        if path:
            cost, nodes = path
            print(f"From {source} to {target}: Path = {nodes}")

    print("\nEdge appearance statistics:")
    print(f"Maximum appearance: {max_app}")
    print(f"Minimum appearance: {min_app}")
    print(f"Average appearance: {avg_app:.2f}")

    # Create graph showing shortest paths
    path_analysis. plot_individual_shortest_paths(initial_graph, selected_paths)

    # Allocate bandwidths
    lightpaths, wavelengths = path_analysis.allocate_bandwidths(selected_paths)

    print("\nLightpaths and assigned wavelengths:")
    for (source, target), wavelength in lightpaths.items():
        print(f"From {source} to {target}: λ{wavelength}")

    print("\nWavelength usage per edge:")
    for edge, wl_set in wavelengths.items():
        print(f"Edge {edge}: Wavelengths = {sorted(wl_set)}")
