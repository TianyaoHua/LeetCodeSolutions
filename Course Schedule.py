class Solution(object):
    def transfer_list_to_adjacency_list(self, n, edge_list):
        adj_list = [[] for i in range(n)]
        for edge in edge_list:
            adj_list[edge[0]].append(edge[1])
        return adj_list

    def DFS(self, n,adj_list):
        color = ['white' for i in range(n)]
        cycle = False
        for node in range(n):
            if color[node] == 'white':
                cycle = cycle or self.DFS_core(adj_list, node, color)
        return cycle

    def DFS_core(self,adj_list,node,color):
        color[node] = 'gray'
        cycle = False
        for neighbour in adj_list[node]:
            if color[neighbour] == 'white':
                cycle = cycle or self.DFS_core(adj_list, neighbour, color)
            elif color[neighbour] == 'gray':
                cycle = True
        color[node] = 'black'
        return cycle

    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        adj_list = self.transfer_list_to_adjacency_list(numCourses, prerequisites)
        cycle = self.DFS(numCourses,adj_list)
        return not cycle


if __name__=="__main__":
    solution = Solution()
    n = 2
    edge_list = [[1,0]]
    print(solution.canFinish(n,edge_list))