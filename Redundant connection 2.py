class Solution(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        A = []
        for edge in edges:
            if edge[0] in A:
                if edge[1] not in A:
                    A.append(edge[1])
                else:
                    return edge
            elif edge[1] in A:
                A.append(edge[0])
            else:
                A.append(edge[0])
                A.append((edge[1]))

if __name__=="__main__":
    solution = Solution()
    edge_list = [[1,5],[3,4],[3,5],[4,5],[2,4]]
    print(solution.findRedundantConnection(edge_list))