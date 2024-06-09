class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adj_list = {i: [] for i in range(vertices)}
        self.edges = []

    def remove_node(self, vertex):
        self.adj_list.pop(vertex,None)
        self.edges=[edge for edge in self.edges if edge[0]!=vertex and edge[1]!=vertex]
        for key in self.adj_list:
            self.adj_list[key]=[item for item in self.adj_list[key] if item[0]!=vertex]

    def add_edge(self, u, v, weight=1):
        self.adj_list[u].append((v,weight))
        self.adj_list[v].append((u,weight))
        self.edges.append((u,v,weight))

    def remove_edge(self, u, v):
        self.adj_list[u]=[item for item in self.adj_list[u] if item[0]!=v]
        self.adj_list[v]=[item for item in self.adj_list[v] if item[0]!=u]
        self.edges=[edge for edge in self.edges if not (edge[0]==u and edge[1]==v) and not(edge[0]==v and edge[1]==u)]
    def bfs(self, start_vertex):
        visited=[False]*self.vertices
        queue=[]
        bfs_order=[]
        queue.append(start_vertex)
        visited[start_vertex]=True
        while queue:
            vertex=queue.pop(0)
            bfs_order.append(vertex)
            for neighbour,weight in self.adj_list[vertex]:
                if not visited[neighbour]:
                    queue.append(neighbour)
                    visited[neighbour]=True
            return bfs_order

    def dfs(self, start_vertex):
        visited=[False]*self.vertices
        dfs_order=[]
        self.dfs_util(start_vertex,visited,dfs_order)
        return dfs_order
    def dfs_util(self,vertex,visited,dfs_order):
        visited[vertex]=True
        dfs_order.append(vertex)
        for neighbour,weight in self.adj_list[vertex]:
            if not visited[neighbour]:
                self.dfs_util(neighbour,visited,dfs_order)
                
    def find(self,parent,i):
        if parent[i]==i:
            return i
        return self.find(parent,parent[i])
    def union(self,parent,rank,x,y):
        xroot=self.find(parent,x)
        yroot=self.find(parent,y)
        if rank[xroot]<rank[yroot]:
            parent[xroot]=yroot
        elif rank[xroot]>rank[yroot]:
            parent[yroot]=xroot
        else:
            parent[yroot]=xroot
            rank[xroot]+=1
    def kruskal(self):
        result=[]
        i,e=0
        self.edges=sorted(self.edges,key=lambda item:item[2])
        parent=[]
        rank=[]
        for node in range(self.vertices):
            parent.append(node)
            rank.append(0)
        while e < self.vertices-1:
            u,v,w=self.edges[i]
            i+=1
            x=self.find(parent,u)
            y=self.find(parent,v)
            if x!=y:
                e+=1
                result.append((u,v,w))
                self.union(parent,rank,x,y)
        return result
    def prim(self):
        import heapq
        min_heap=[(0,0)]
        mst=[]
        total_cost=0
        visited=set()
        while min_heap:
            weight,u=heapq.heappop(min_heap)
            if u in visited:
                continue
            visited.add(u)
            total_cost+=weight
            mst.append((u,weight))
            for v,w in self.adj_list[u]:
                if v not in visited:
                    heapq.heappush(min_heap,(w,v))
        return mst,total_cost
    
    def dijkstra(self, start_vertex):
        import heapq
        distances={i:float('inf') for i in range(self.vertices)}
        distances[start_vertex]=0
        pq=[(0,start_vertex)]
        while pq:
            current_distance,current_vertex=heapq.heappop(pq)
            if current_distance>distances[current_vertex]:
                continue
            for neighbour,weight in self.adj_list[current_vertex]:
                distance=current_distance+weight
                if distance<distances[neighbour]:
                    distances[neighbour]=distance
                    heapq.heappush(pq,(distance,neighbour))
        return distances
    
    def graph_size(self):
        return self.vertices

    def get_neighbors(self, vertex):
        return self.adj_list[vertex]

    def print_graph(self):
        for vertex in self.adj_list:
            print(f"Vertex {vertex}:{self.adj_list[vertex]}")

# Driver code
def testGraph():
    vertices = int(input())
    graph = Graph(vertices)

    while True:
        command = input().strip()
        if command == "End":
            break

        operation = command.split()
        cmd_type = operation[0]

        if cmd_type == "AddEdge":
            u, v, w = int(operation[1]), int(operation[2]), int(operation[3])
            graph.add_edge(u, v, w)
            print(f"Edge added between {u} and {v} with weight {w}")
        
        elif cmd_type == "RemoveEdge":
            u, v = int(operation[1]), int(operation[2])
            graph.remove_edge(u, v)
            print(f"Edge removed between {u} and {v}")

        elif cmd_type == "RemoveNode":
            vertex = int(operation[1])
            graph.remove_node(vertex)
            print(f"Node {vertex} removed")

        elif cmd_type == "BFS":
            start_vertex = int(operation[1])
            result = graph.bfs(start_vertex)
            print(f"BFS from vertex {start_vertex}: {result}")

        elif cmd_type == "DFS":
            start_vertex = int(operation[1])
            result = graph.dfs(start_vertex)
            print(f"DFS from vertex {start_vertex}: {result}")

        elif cmd_type == "MST":
            algo = operation[1]
            if algo == "Kruskal":
                result = graph.kruskal()
                print(f"MST (Kruskal's): {result}")
            elif algo == "Prim":
                result = graph.prim()
                print(f"MST (Prim's): {result}")

        elif cmd_type == "ShortestPath":
            start_vertex = int(operation[1])
            result = graph.dijkstra(start_vertex)
            print(f"Shortest paths from vertex {start_vertex}: {result}")

        elif cmd_type == "Print":
            graph.print_graph()

def main():
    testGraph()

if __name__ == "__main__":
    main()