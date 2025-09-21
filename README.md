# 🌐 Optical Communication Networks – k Shortest Path Routing & Wavelength Assignment

[![Python](https://img.shields.io/badge/Python-3.10+-blue)](https://www.python.org/)
[![NetworkX](https://img.shields.io/badge/Lib-NetworkX-green)](https://networkx.org/)
[![Matplotlib](https://img.shields.io/badge/Lib-Matplotlib-orange)](https://matplotlib.org/)

This repository contains the implementation of the **k-shortest path routing algorithm** and **wavelength assignment in optical networks**.  
The project is divided into three main parts:

---

## 📖 Theory & Methodology

### 1. K-Shortest Path Routing
- Implements **Dijkstra's algorithm** to find the shortest path between nodes in a network.  
- Extends Dijkstra’s algorithm to compute the **k-shortest paths** between all source-destination pairs.  
- Uses a **priority queue (heapq)** to iteratively expand paths in increasing order of cost.  
- Avoids loops by preventing revisits to nodes already in the path.  
- Visualizes the **network topology** and computed routes with **NetworkX** and **Matplotlib**.

### 2. Path Analysis
- Selects the **shortest path** for each source-destination pair from the computed k paths.  
- Tracks **link usage frequency** across all selected paths.  
- Computes statistics:
  - Maximum number of times a link is used  
  - Minimum usage  
  - Average usage across the network  
- Identifies **bottleneck edges** that appear frequently in multiple paths.  

### 3. Wavelength Assignment
- Implements three **wavelength allocation strategies** for lightpaths:
  - **Random Fit** – picks a random available wavelength  
  - **First Fit** – assigns the first available wavelength in ascending order  
  - **Least Used** – balances load by selecting the wavelength with the fewest assignments  
- Ensures that:
  - No two lightpaths on the **same link** share the same wavelength.  
  - Each lightpath uses the **same wavelength across all its links**.  
- Compares the algorithms based on:
  - **Blocking percentage** – percentage of unserved connection requests  
  - **Execution time** – computational performance  

---

## 📂 Repository Structure
- `main_a.py` / `main_b.py` → Implements k-shortest path routing and path analysis  
- `main_c.py` → Implements wavelength assignment (Random Fit, First Fit, Least Used)  
- `dijkstra_shortest_path.py` → Core Dijkstra and k-shortest path implementation  
- `path_analysis.py` → Shortest path selection and link usage statistics  
- `wavelength_assignment.py` → Wavelength allocation algorithms  

---

## ⚙️ Requirements
- Python 3.10+  
- Libraries: `networkx`, `matplotlib`, `heapq`, `random`, `time`  

Install dependencies:
```bash
pip install networkx matplotlib
