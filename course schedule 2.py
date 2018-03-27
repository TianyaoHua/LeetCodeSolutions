class Solution(object):
    def transfer_list_to_adjacency_list(self, n, edge_list):
        adj_list = [[] for i in range(n)]
        for edge in edge_list:
            adj_list[edge[0]].append(edge[1])
        return adj_list

    def DFS(self, n, adj_list):
        color = ['white' for i in range(n)]
        cycle = False
        time = 0
        topological_order = []
        discover_time = [0 for i in range(n)]
        finish_time = [0 for i in range(n)]
        for node in range(n):
            if color[node] == 'white':
                cycle = cycle or self.DFS_core(adj_list, node, color, time, discover_time,finish_time,topological_order)
        return cycle, topological_order

    def DFS_core(self,adj_list,node,color,time, discover_time,finish_time,topological_order):
        color[node] = 'gray'
        cycle = False
        time += 1
        discover_time[node] = time
        for neighbour in adj_list[node]:
            if color[neighbour] == 'white':
                cycle = cycle or self.DFS_core(adj_list, neighbour, color,time,discover_time,finish_time,topological_order)
            elif color[neighbour] == 'gray':
                cycle = True
        color[node] = 'black'
        time += 1
        finish_time[node] = time
        topological_order.append(node)   #it is reverse_topologicacl order
        return cycle

    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """

        adj_list = self.transfer_list_to_adjacency_list(numCourses, prerequisites)
        cycle, topological_order= self.DFS(numCourses,adj_list)
        if cycle:
            return []
        else:
            return topological_order

if __name__=="__main__":
    solution = Solution()
    n = 2
    edge_list = [[1,0]]
    print(solution.findOrder(n,edge_list))