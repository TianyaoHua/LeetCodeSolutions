class Solution(object):
    def transfer_list_to_adjacency_list(self, edge_list):
        adj_list = {}
        for edge in edge_list:
            if edge[0] not in adj_list:
                adj_list.update({edge[0]: []})
            adj_list[edge[0]].append(edge[1])
            if edge[1] not in adj_list:
                adj_list.update({edge[1]: []})
            adj_list[edge[1]].append(edge[0])
        return adj_list

    def DFS(self, adj_list):
        color = {}
        p = {}
        for node in adj_list:
            color.update({node: 'white'})
            p.update({node: None})
        for node in adj_list:
            if color[node] == 'white':
                cycle = self.DFS_core(adj_list, node, color, p)
                if cycle:
                    return cycle, p

    def DFS_core(self, adj_list, node, color, p):
        color[node] = 'gray'
        cycle = None
        for neighbor in adj_list[node]:
            if color[neighbor] == 'white':
                p[neighbor] = node
                cycle_below = self.DFS_core(adj_list, neighbor, color, p)
                if cycle_below:
                    cycle = cycle_below
            elif color[neighbor] == 'gray' and p[node] != neighbor:
                p[neighbor] = node
                cycle = node
        color[node] = 'black'
        return cycle

    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        adj_list = self.transfer_list_to_adjacency_list(edges)
        cycle, p =self.DFS(adj_list)
        node = cycle
        if p[node] < node:
            target = [p[node], node]
        else:
            target = [node, p[node]]
        while p[node] != cycle:
            if p[node] < node and edges.index([p[node], node]) > edges.index(target):
                target = [p[node], node]
            elif p[node] > node and edges.index([node, p[node]]) > edges.index(target):
                target = [node, p[node]]
            node = p[node]
        if p[node] < node and edges.index([p[node], node]) > edges.index(target):
            target = [p[node], node]
        elif p[node] > node and edges.index([node, p[node]]) > edges.index(target):
            target = [node, p[node]]
        return target

if __name__=="__main__":
    solution = Solution()
    edge_list = [[1,5],[3,4],[3,5],[4,5],[2,4]]
    print(solution.findRedundantConnection(edge_list))