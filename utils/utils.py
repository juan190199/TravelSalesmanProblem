import copy
import networkx as nx

from graph import Graph

def create_graph():
    """

    :return:
    """
    ...


def get_mst(graph):
    """
    Kruskal's algorithm
    :param graph:
    :return:
    """
    edges = graph.get_edges()
    weighted_edges = {}
    for (u, v) in edges:
        weighted_edges[(u, v)] = int(graph.get_edge_weight(u, v))

    # Sort edges by weight, by value
    weighted_edges = sorted(weighted_edges.items(), key=lambda x: x[1])

    mst_graph = Graph()
    nodes = []
    for itm in weighted_edges:
        u, v = itm[0]
        mst_graph.add_edge(u, v, graph.get_edge_weight(u, v))
        try:
            nx.algorithms.find_cycle(mst_graph.get_graph())
            mst_graph.get_graph().remove_edge(u, v)
        except nx.NetworkXNoCycle:
            nodes.append(u)
            nodes.append(v)

    return mst_graph


def get_degrees(graph):
    """

    :param graph:
    :return:
    """
    degrees = {}

    for d in graph.get_degree():
        degrees[d[0]] = d[1]

    return degrees


def get_nodes_odd_degrees(degrees):
    """
    
    :param degrees: 
    :return: 
    """
    odd_degrees = {}

    for k in degrees.keys():
        if (degrees[k] % 2 != 0):
            odd_degrees[k] = degrees[k]

    return odd_degrees


def print_edges_with_weight(graph):
    """

    :param graph:
    :return:
    """
    if isinstance(graph.get_graph(), nx.MultiGraph):
        for e in graph.get_edges():
            print(f"Edge: ({e[0]}, {e[1]})")
    else:
        for e in graph.get_edges():
            print(f"Edge: ({e[0]}, {e[1]}) = {graph.get_edge_weight(e[0], e[1])}")


def create_minimum_weight_perfect_matching(graph):
    """

    :param graph:
    :return:
    """
    ...


def union_graphs(graph1, graph2):
    """

    :param graph1:
    :param graph2:
    :return:
    """
    ...


def get_total_cost(graph, path):
    """

    :param graph:
    :param path:
    :return:
    """
    ...
