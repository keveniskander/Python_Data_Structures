"""
-------------------------------------------------------
graphs.py
-------------------------------------------------------
Author:  Keven Iskander
ID:      160634540
Email:   iska4540@mylaurier.ca
__updated__ = "2017-02-19"
-------------------------------------------------------
"""


class Edge:

    def __init__(self, start, end, distance):
        """
        -------------------------------------------------------
        Initializes an Edge object.
        Use: e = Edge(start, end, distance)
        -------------------------------------------------------
        Preconditions:
            start - starting node name (?)
            end - ending node name (?)
            distance - distance between start and end (int > 0)
        Postconditions:
            The edge is initialized.
        -------------------------------------------------------
        """
        self.start = start
        self.end = end
        self.distance = distance
        return

    def reverse(self):
        """
        -------------------------------------------------------
        Returns an Edge object with the start and end nodes reversed.
        Use: e2 = e1.reverse()
        -------------------------------------------------------
        Postconditions:
            returns
            new_edge - an Edge object with the node names swapped (Edge)
        -------------------------------------------------------
        """
        new_edge = Edge(self.end, self.start, self.distance)
        return new_edge

    def __str__(self):
        """
        -------------------------------------------------------
        Returns a string representation of the edge.
        Use: s = str(e) or print(e)
        -------------------------------------------------------
        Postconditions:
            Returns a string representation of the edge.
        -------------------------------------------------------
        """
        return "{} -> {}: {}".format(self.start, self.end, self.distance)

    def __eq__(self, rs):
        """
        -------------------------------------------------------
        Compares two edges for equality of distance.
        Use: e == rs
        -------------------------------------------------------
        Preconditions:
            rs - another edge (Edge)
        Postconditions:
            Returns whether the distance of two edges are the same.
        -------------------------------------------------------
        """
        return self.distance == rs.distance

    def __lt__(self, rs):
        """
        -------------------------------------------------------
        Compares distance of two edges.
        Use: e < rs
        -------------------------------------------------------
        Preconditions:
            rs - another edge (Edge)
        Postconditions:
            Returns True if distance of edge < distance of rs, False otherwise.
        -------------------------------------------------------
        """
        return self.distance < rs.distance

    def le(self, rs):
        """
        -------------------------------------------------------
        Compares distance of two edges.
        Use: e <= rs
        -------------------------------------------------------
        Preconditions:
            rs - another edge (Edge)
        Postconditions:
            Returns True if distance of edge <= distance of rs,
                False otherwise.
        -------------------------------------------------------
        """
        return self == rs or self < rs


class Graph:

    def __init__(self, edges):
        """
        -------------------------------------------------------
        Initializes a Graph object.
        Use: g = Graph(edges)
        -------------------------------------------------------
        Preconditions:
            edges - a list of Edge objects - each edge may appear
                only once in the list (list of Edge)
        Postconditions:
            The graph is initialized. Edges are stored in a dictionary
                keyed by node name.
        -------------------------------------------------------
        """
        self._nodes = dict()

        for edge in edges:
            # Store the edge with its start node name.
            node_name = edge.start

            if node_name not in self._nodes:
                self._nodes[node_name] = list()
            self._nodes[node_name].append(edge)

            # Store the reversed edge with its start node name.
            r_edge = edge.reverse()
            node_name = r_edge.start

            if node_name not in self._nodes:
                self._nodes[node_name] = list()

            self._nodes[node_name].append(r_edge)
        return

    def __len__(self):
        """
        -------------------------------------------------------
        Returns the number of nodes in the graph.
        Use: n = len(g)
        -------------------------------------------------------
        Postconditions:
            returns number of node names in graph (int)
        -------------------------------------------------------
        """
        return len(self._nodes)

    def node_names(self):
        """
        -------------------------------------------------------
        Returns a sorted list of graph node names.
        Use: names = g.node_names()
        -------------------------------------------------------
        Postconditions:
            returns
            a sorted list of all graph node names (list of str)
        -------------------------------------------------------
        """
        return sorted(self._nodes.keys())

    def edges_by_node(self, node_name):
        """
        -------------------------------------------------------
        Returns all the edges radiating out from node_name.
        Use: edges = g.edges_by_node(node_name)
        -------------------------------------------------------
        Preconditions:
            node_name - a node name in the graph (str)
        Postconditions:
            returns
            edges - a list of all the edges staring at node_name (list of Edge)
        -------------------------------------------------------
        """
        edges = self._nodes[node_name]
        return edges


def graph_test(data):
    """
    -------------------------------------------------------
    Demonstrates use of Graph class.
    Use: graph_test(data)
    -------------------------------------------------------
    Preconditions:
        data - graph edges stored in tuples, where each tuple contains
            an edge start, end, and distance (tuple of (str, str, int))
    Postconditions:
        prints
        all node names and edges in the graph
    -------------------------------------------------------
    """
    edges = []

    for d in data:
        edge = Edge(d[0], d[1], d[2])
        edges.append(edge)

    # Initialize the graph.
    graph = Graph(edges)

    node_names = graph.node_names()

    for node_name in node_names:
        print("Node: {}".format(node_name))
        node_edges = graph.edges_by_node(node_name)

        for edge in node_edges:
            print(edge)
        print()
    return