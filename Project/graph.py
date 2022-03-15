import csv

distanceFilename ='D:\C950\Project\WGUPS_ Distance_Table.csv' #'WGUPS_Distance_Table.csv'

class Graph:
    def __init__(self):
        #I will probably build some kind of adjacency list building function for this.
        self.adjacency_list = {}
        self.edge_weights = {}
    def add_vertex(self, new_vertex):
        self.adjacency_list[new_vertex] = []
    def add_directed_edge(self, from_vertex, to_vertex, weight = 1.0):
        self.edge_weights[(from_vertex, to_vertex)] = weight
        self.adjacency_list[from_vertex].append(weight)
    def add_undirected_edge(self, vertex_a, vertex_b, weight = 1.0):
        self.add_directed_edge(vertex_a, vertex_b, weight)
        self.add_directed_edge(vertex_b, vertex_a, weight)



def loadDistanceData(filename):

    #I now have two lists: One with address and distance data and another with address data.
    distanceList = []
    addressList = []
    count = 0
    with open(filename) as csvFile:
        #remove the \n newline
        cleaned = (line.replace('\n', '') for line in csvFile)

        distanceData = csv.reader(cleaned, delimiter=',')
        #skip first row
        next(distanceData)
        next(distanceData)
        #append each row to distanceList

        for row in distanceData:
            distanceList.append(row)
        print(distanceList)
        
        for row in range(len(distanceList)):
            addressList.append(distanceList[row][0])


        print(addressList)
    return distanceList

        #addressList = distanceList[0]
        #print(addressList)
        #distanceList.remove(distanceList[0])
'''
def create_graph(filename):
    distances = loadDistanceData(filename)
    graph_distances = Graph()
    for row in distances:
        graph_distances.add_vertex(row[0])
    distances.remove(distances[0])
    print(graph_distances.adjacency_list)
    #print(graph_distances.edge_weights)\
    count = 2
    for row in distances:
        for i in range(count, len(row)):
            if row[i] is '':
                print('empty')
                break
            print(i)
            print(row[0])
            print(distances[i-1][0])
            print(row[i])
            graph_distances.add_undirected_edge(row[0], distances[i-1][0], float(row[2]))
            print(graph_distances.adjacency_list)
    return graph_distances


print(create_graph(distanceFilename))
'''
loadDistanceData(distanceFilename)

