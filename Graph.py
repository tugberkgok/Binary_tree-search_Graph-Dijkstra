class Graph:
    def __init__(self, num_node, edges):
        self.node = num_node
        self.data = [[] for _ in range(num_node)]
        for n1, n2 in edges:
            self.data[n1].append(n2)
            self.data[n2].append(n1)

    def add_edge(self,n1,n2):
        self.data[n1].append(n2)
        self.data[n2].append(n1)
    def remove_edge(self,n1,n2):
        self.data[n1].remove(n2)
        self.data[n2].remove(n1)

    def __repr__(self):
        return "\n".join(["{}:{}".format(n, neighbour) for n, neighbour in enumerate(self.data)])

    def __str__(self):
        return self.__repr__()


class Matrix:
    def __init__(self, num_node, edges):
        self.table = [[0 for _ in range(num_node)] for _ in range(num_node)]
        for n1, n2 in edges:
            self.table[n1][n2] = 1
            self.table[n2][n1] = 1

    def add_edge(self, n1, n2):
        self.table[n1][n2] = 1
        self.table[n2][n1] = 1

    def remove_edge(self, n1, n2):
        self.table[n1][n2] = 0
        self.table[n2][n1] = 0

    def __repr__(self):
        return "\n".join(["{}:{}".format(n, neighbour) for n, neighbour in enumerate(self.table)])

    def __str__(self):
        return self.__repr__()

def BFS(graph, root):
    queue = []
    copy = []
    label = [False]*len(graph.data)
    queue.append(root)
    label[root] = True
    while len(queue) > 0:
        v = queue.pop(0)
        copy.append(v)
        for node in graph.data[v]:
            if label[node] == False:
                label[node] = True
                queue.append(node)
    return copy
def BFS3(graph,num_nodes):
    visited = [False] * num_nodes
    item = 0
    count = 0
    while item < num_nodes:
        if not visited[item]:
            queue = []
            visited[item] = True
            queue.append(item)
            i = 0
            while i < len(queue):
                current = queue[i]
                i+=1
                for v in graph.data[current]:
                    if not visited[v]:
                        visited[v] = True
                        queue.append(v)
            count += 1
            print("Connected component {}:{}".format(count,queue))
        item+=1

def DFS(graph, source):
    stack = []
    result = []
    label = [False]*len(graph.data)
    stack.append(source)
    while len(stack) > 0:
        node = stack.pop()
        if not label[node]:
            label[node] = True
            result.append(node)
            for v in graph.data[node]:
                if not label[v]:
                    stack.append(v)
    return result


num_node = 5
edges = [(0,1),(0,4),(1,4),(3,1),(2,1),(4,3),(2,3)]
len(edges)
graph1 = Graph(num_node,edges)
graph2= Matrix(num_node,edges)
print(graph1)
print(graph2)

