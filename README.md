# K-Shortest Path Routing and Wavelength Assignment in Optical Networks

This repository contains the implementation of the k-shortest path routing algorithm and wavelength assignment in optical networks. The project is divided into three main parts:

1. **K-Shortest Path Routing**
* Implements Dijkstra's algorithm to find the shortest paths between nodes in a network.
* Extends Dijkstra's algorithm to find the k-shortest paths between all pairs of nodes.
*  Visualizes the network topology and the computed paths using networkx and matplotlib.

2. **Path Analysis**
* Analyzes the computed paths to select the shortest path for each source-destination pair.
* Counts the frequency of each link in the selected paths and calculates statistics such as maximum, minimum, and average link usage.

3. **Wavelength Assignment**
* Implements three wavelength assignment algorithms (Random Fit, First Fit, and Least Used) to allocate wavelengths to lightpaths in the network.
* Ensures that no two lightpaths sharing a common link are assigned the same wavelength.
* Compares the performance of the three algorithms in terms of blocking percentage and execution time.

**Repository Structure**
* main_a,b.py: Implements k-shortest path routing and path analysis.
* main_c.py: Implements wavelength assignment using Random Fit, First Fit, and Least Used algorithms.
* dijkstra_shortest_path.py: Contains the implementation of Dijkstra's algorithm.
* path_analysis.py: Analyzes the selected paths and calculates link usage statistics.
* wavelength_assignment.py: Implements the wavelength assignment algorithms.
