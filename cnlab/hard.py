import networkx as nx
import time
import random

def centralized_routing(nodes):
    # Create a random graph with given number of nodes
    G = nx.fast_gnp_random_graph(nodes, 0.2)
    for (u, v) in G.edges():
        G.edges[u, v]['weight'] = random.randint(1, 10)  # Random edge weights

    start_time = time.time()
    # Perform centralized routing using Dijkstra's algorithm
    shortest_paths = {}
    for node in G.nodes():
        shortest_paths[node] = nx.single_source_dijkstra_path_length(G, node)

    end_time = time.time()
    total_time = end_time - start_time

    # Calculate total CPU cycles and communication bits
    total_cpu_cycles = nodes * nodes  # Assuming one CPU cycle per edge traversal
    total_communication_bits = nodes * nodes  # Assuming one bit per edge

    return total_time, total_cpu_cycles, total_communication_bits

def decentralized_routing(nodes):
    # Create a random graph with given number of nodes
    G = nx.fast_gnp_random_graph(nodes, 0.2)
    for (u, v) in G.edges():
        G.edges[u, v]['weight'] = random.randint(1, 10)  # Random edge weights

    start_time = time.time()
    # Perform decentralized routing using Distance Vector Routing (DVR) algorithm
    # Initialize distance vectors for each node
    distance_vectors = {}
    for node in G.nodes():
        distance_vectors[node] = {}
        for neighbor in G.neighbors(node):
            distance_vectors[node][neighbor] = G.edges[node, neighbor]['weight']
        distance_vectors[node][node] = 0  # Distance to self is 0

    # Iteratively update distance vectors
    updated = True
    while updated:
        updated = False
        for node in G.nodes():
            for neighbor in G.neighbors(node):
                for dest_node in G.nodes():
                    new_distance = distance_vectors[node][neighbor] + distance_vectors[neighbor][dest_node]
                    if new_distance < distance_vectors[node][dest_node]:
                        distance_vectors[node][dest_node] = new_distance
                        updated = True

    end_time = time.time()
    total_time = end_time - start_time

    # Calculate total CPU cycles and communication bits
    total_cpu_cycles = nodes * nodes * nodes  # Assuming one CPU cycle per comparison/update
    total_communication_bits = nodes * nodes * nodes  # Assuming one bit per comparison/update

    return total_time, total_cpu_cycles, total_communication_bits

# Perform analysis for different numbers of nodes
nodes_list = [10, 100, 1000, 10000, 100000]
for nodes in nodes_list:
    print(f"Number of nodes: {nodes}")
    central_time, central_cycles, central_bits = centralized_routing(nodes)
    print(f"Centralized routing - Time: {central_time:.4f}s, CPU cycles: {central_cycles}, Communication bits: {central_bits}")

    decentralized_time, decentralized_cycles, decentralized_bits = decentralized_routing(nodes)
    print(f"Decentralized routing - Time: {decentralized_time:.4f}s, CPU cycles: {decentralized_cycles}, Communication bits: {decentralized_bits}\n")
