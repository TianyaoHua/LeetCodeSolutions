class Solution(object):
    def transfer_list_to_adjacency_list(self, edge_list, values):
        adj_list = {}
        w = {}
        n = len(edge_list)
        for i in range(n):
            if edge_list[i][0] not in adj_list:
                adj_list.update({edge_list[i][0]: [edge_list[i][1]]})
                w.update({edge_list[i][0]+edge_list[i][1]: values[i]})
                w.update({edge_list[i][1]+edge_list[i][0]: 1/values[i]})
            else:
                adj_list[edge_list[i][0]].append(edge_list[i][1])
                w.update({edge_list[i][0]+edge_list[i][1]: values[i]})
                w.update({edge_list[i][1]+edge_list[i][0]: 1/values[i]})
            if edge_list[i][1] not in adj_list:
                adj_list.update({edge_list[i][1]: [edge_list[i][0]]})
            else:
                adj_list[edge_list[i][1]].append(edge_list[i][0])
        return adj_list, w

    def BFS(self, adj_list, u, v, w):
        if u not in adj_list or v not in adj_list:
            return -1
        d = {}
        color = {}
        for node in adj_list:
            color.update({node: 'white'})
            d.update({node: -1})
        q = [u]
        d[u] = 1
        while q:
            node = q[0]
            q.remove(node)
            for neighbour in adj_list[node]:
                if color[neighbour] == 'white':
                    color[neighbour] = 'gray'
                    d[neighbour] = d[node]*w[(node+neighbour)]
                    q.append(neighbour)
            color[node] = 'black'
        return d[v]

    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        answer = []
        adj_list, w = self.transfer_list_to_adjacency_list(equations, values)
        for question in queries:
            answer.append(self.BFS(adj_list, question[0], question[1], w))
        return answer

if __name__ == "__main__":

    solution = Solution()
    equations = [["a", "b"], ["b", "c"]]
    values = [2.0, 3.0]
    queries = [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]
    print(solution.calcEquation(equations, values, queries))