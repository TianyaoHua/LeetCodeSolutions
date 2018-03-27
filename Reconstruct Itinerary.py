class Solution(object):

    def transfer_list_to_adjacency_list(self, edge_list):
        adj_list = {}
        out_degree_list = {}
        for edge in edge_list:
            if edge[0] not in adj_list:
                adj_list.update({edge[0]: [edge[1]]})
                out_degree_list.update({edge[0]: 1})
            else:
                adj_list[edge[0]].append(edge[1])
                out_degree_list[edge[0]] += 1
        for node in adj_list:
            adj_list[node].sort(reverse=True)
        return adj_list, out_degree_list

    def euler_tour(self, adj_list, s):
        T = []
        while adj_list:
            if not T:
                node = s
                q = [s]
            else:
                n = len(T)-1
                while T[n] not in adj_list:
                    n -= 1
                node = T[n]
                q = [node]
            while node in adj_list:
                neighbour = adj_list[node][-1]
                q.append(neighbour)
                adj_list[node].pop()
                if not adj_list[node]:
                    adj_list.pop(node)
                node = neighbour
            if not T:
                T = q
            else:
                print(T)
                print(q)
                index = len(T)-T[::-1].index(q[0])
                T[index: index] = q[1:]
        return T

    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        adj_list, out_degree_list = self.transfer_list_to_adjacency_list(tickets)
        T = self.euler_tour(adj_list,'JFK')
        return T

if __name__=="__main__":
    solution = Solution()
    tickets = [["AXA","AUA"],["BNE","ANU"],["EZE","ANU"],["TIA","JFK"],["TIA","BNE"],["ANU","BNE"],["BNE","AUA"],["BNE","ADL"],["AXA","ADL"],["EZE","AUA"],["AUA","AXA"],["ADL","AXA"],["ADL","TIA"],["JFK","ANU"],["EZE","JFK"],["JFK","AUA"],["BNE","EZE"],["TIA","ANU"],["TIA","AUA"],["JFK","TIA"],["EZE","ANU"],["AXA","JFK"],["AUA","OOL"],["AUA","AXA"],["ANU","BNE"],["ANU","EZE"],["ANU","TIA"],["JFK","EZE"],["ADL","ANU"],["AXA","BNE"],["BNE","ADL"],["ANU","EZE"],["ANU","JFK"],["BNE","AUA"],["ANU","AUA"],["ANU","AXA"],["TIA","BNE"],["AUA","EZE"],["JFK","ANU"],["AXA","TIA"],["EZE","ANU"],["AUA","BNE"],["AUA","AXA"],["AUA","TIA"]]
    print(solution.transfer_list_to_adjacency_list(tickets))
    print(solution.findItinerary(tickets))
