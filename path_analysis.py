import networkx as nx
import matplotlib.pyplot as plt


def analyze_paths(all_paths):
    edge_counts = {}  # Dictionary to count appearances of edges
    selected_paths = {}  # Dictionary to store selected paths

    for (source, target), paths in all_paths.items():
        # Select the path with the least number of edges
        selected_path = min(paths, key=lambda x: len(x[1])) if paths else None
        selected_paths[(source, target)] = selected_path

        # Count the edges in the selected path
        if selected_path:
            _, path = selected_path
            for i in range(len(path) - 1):
                edge = tuple(sorted((path[i], path[i + 1])))  # Treat bidirectional edges as the same
                edge_counts[edge] = edge_counts.get(edge, 0) + 1

    # Calculate maximum, minimum, and average edge appearances
    if edge_counts:
        max_appearance = max(edge_counts.values())
        min_appearance = min(edge_counts.values())
        avg_appearance = sum(edge_counts.values()) / len(edge_counts)
    else:
        max_appearance = min_appearance = avg_appearance = 0

    return selected_paths, edge_counts, max_appearance, min_appearance, avg_appearance


def allocate_bandwidths(selected_paths):
    wavelengths = {}  # Dictionary to store wavelengths for each edge
    lightpaths = {}   # Dictionary to store the wavelength for each path
    l = 1  # Initialize the wavelength variable

    for (source, target), path_info in selected_paths.items():
        if path_info:
            _, path = path_info

            # Determine the set of unavailable wavelengths for this path
            unavailable_wavelengths = set()
            for i in range(len(path) - 1):
                edge = tuple(sorted((path[i], path[i + 1])))  # Treat bidirectional edges as the same
                if edge in wavelengths:
                    unavailable_wavelengths.update(wavelengths[edge])

            # Assign the first available wavelength not in use on any edge in the path
            assigned_wavelength = None
            for candidate in range(1, l + 1):
                if candidate not in unavailable_wavelengths:
                    assigned_wavelength = candidate
                    break

            # If no available wavelength exists, assign a new one
            if assigned_wavelength is None:
                l += 1
                assigned_wavelength = l

            lightpaths[(source, target)] = assigned_wavelength

            # Assign the wavelength to all edges in the path
            for i in range(len(path) - 1):
                edge = tuple(sorted((path[i], path[i + 1])))  # Treat bidirectional edges as the same
                if edge not in wavelengths:
                    wavelengths[edge] = set()
                wavelengths[edge].add(assigned_wavelength)

    return lightpaths, wavelengths


def create_graph(matrix):
    g = nx.Graph()
    n = len(matrix)
    for i in range(n):
        for j in range(n):
            if matrix[i][j] > 0:
                g.add_edge(i + 1, j + 1, weight=matrix[i][j])
    return g


def plot_graph(g, title, paths=None):
    pos = nx.spring_layout(g)  # Layout for graph visualization
    edge_labels = nx.get_edge_attributes(g, 'weight')

    plt.figure(figsize=(8, 6))
    nx.draw(g, pos, with_labels=True, node_color='lightblue', node_size=700, font_size=12)
    nx.draw_networkx_edge_labels(g, pos, edge_labels=edge_labels)

    if paths:
        for path in paths.values():
            if path:
                _, nodes = path
                edges = [(nodes[i], nodes[i + 1]) for i in range(len(nodes) - 1)]
                nx.draw_networkx_edges(g, pos, edgelist=edges, edge_color='red', width=2)

    plt.title(title)
    plt.savefig('og_graph.png', bbox_inches='tight')
    plt.show()


def plot_individual_shortest_paths(g, selected_paths):
    pos = nx.spring_layout(g)

    for (source, target), path in selected_paths.items():
        if path:
            _, nodes = path
            edges = [(nodes[i], nodes[i + 1]) for i in range(len(nodes) - 1)]

            plt.figure(figsize=(8, 6))
            nx.draw(g, pos, with_labels=True, node_color='lightblue', node_size=700, font_size=12)
            nx.draw_networkx_edges(g, pos, edgelist=edges, edge_color='red', width=2)

            plt.title(f"Shortest Path: {source} -> {target}")
            plt.savefig(f"{source}_{target}_graph.png", bbox_inches='tight')
            plt.show()
