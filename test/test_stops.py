import networkx as nx
import matplotlib.pyplot as plt
from stops import Stop

stop_id = [100, 101, 102, 103, 201]
bus_stop = ['Lebak Bulus', 'Ciputat', 'Pondok Cabe', 'Gaplek', 'Kampung Rambutan']
num_plat = [8, 2, 4, 4, 12]

def main():
    # create stops
    stops = [Stop(name=c[1], id=c[0], num_platform=c[2]) for c in zip(stop_id, bus_stop, num_plat)]

    # create a graph
    G = nx.Graph()
    G.add_node(stops[0].get_name(), data=stops[0])
    G.add_node(stops[1].get_name(), data=stops[1])
    G.add_node(stops[2].get_name(), data=stops[2])
    G.add_node(stops[3].get_name(), data=stops[3])
    G.add_node(stops[4].get_name(), data=stops[4])

    # create a route
    G.add_edges_from([('Gaplek', 'Ciputat'), ('Ciputat', 'Lebak Bulus')])
    G.add_edges_from([('Kampung Rambutan', 'Lebak Bulus')])
    G.add_edges_from([('Pondok Cabe', 'Lebak Bulus')])

    # access
    for node in G.nodes:
        print('num of bus stop at {}: {}'.format(node, G.nodes[node]['data'].get_platform()))

    nx.draw(G, with_labels=True)

    plt.draw()
    plt.show()

    pass

if __name__ == '__main__':
    main()