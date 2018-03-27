import os
import numpy
class Solution(object):
    def transfer_list_to_adjacency_list(self, n, edge_list):
        adj_list = [[] for i in range(n)]
        for edge in edge_list:
            adj_list[edge[0]].append(edge[1])
            adj_list[edge[1]].append(edge[0])
        return adj_list

    def BFS(self, n, edge_list, s):
        d = [float('inf') for i in range(n)]
        d[s] = '0'
        color = ['white' for i in range(n)]
        Q = [s]
        color[s] = 'gray'
        while Q:
            node = Q[0]
            Q.remove(node)
            for neighbour in edge_list[node]:
                if color[neighbour] == 'white':
                    color[neighbour] = 'gray'
                    d[neighbour] = d[node] + 1
                    Q.append(neighbour)
            color[node] = 'black'

    def DFS(self, n, adj_list):
        color = ['white' for i in range(n)]
        c = ['' for i in range(n)]
        for node in range(n):
            if color[node] == 'white':
                c[node] = '0'
                self.DFS_core(adj_list, node, color, c)
        return c

    def DFS_core(self,adj_list,node,color, c):
        color[node] = 'gray'
        i = -1
        for neighbour in adj_list[node]:
            if color[neighbour] == 'white':
                i += 1
                c[neighbour] = c[node]+str(i)
                self.DFS_core(adj_list, neighbour, color, c)
        color[node] = 'black'

    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        adj_list = self.transfer_list_to_adjacency_list(n, edges)
        c = self.DFS(n, adj_list)
        d = [[float('inf') for i in range(n)] for j in range(n)]
        for i in range(n):
            ci = c[i]
            l_ci = len(ci)
            for j in range(n):
                if j < i:
                    d[i][j] = d[j][i]
                else:
                    d[i][j] = l_ci + len(c[j])-2*len(os.path.commonprefix([ci, c[j]]))
        max_height = [numpy.max(d[i]) for i in range(n)]
        min_height = numpy.min(max_height)
        min_height_root = []
        for i in range(n):
            if min_height == max_height[i]:
                min_height_root.append(i)
        return min_height_root

if __name__=="__main__":
    solution = Solution()
    n = 4
    edge_list = [[1, 0], [1, 2], [1, 3]]
    print(solution.findMinHeightTrees(n, edge_list))