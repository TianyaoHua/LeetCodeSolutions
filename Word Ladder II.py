class Solution(object):
    def BFS(self, graph, s, t):
        Q = [s]
        n = len(s)
        d = {}
        color = {}
        p = {}
        for node in graph:
            color.update({node: 1})
            d.update({node: float('inf')})
            p.update({node: []})
        color[s] = 0
        d[s] = 0
        while Q:
            u = Q.pop(0)
            for i in range(n):
                for c in 'qwertyuiopasdfghjklzxcvbnm':
                    v = u[:i] + c + u[i+1:]
                    if v in graph:
                        if v != u and color[v]:
                            d[v] = d[u] + 1
                            Q.append(v)
                            p[v].append(u)
                            color[v] = 0
                        elif d[v] == d[u] + 1:
                            p[v].append(u)
        if d[t] < float('inf'):
            return p
        else:
            return 0

    def DFS(self, graph, u, answer, solution):
        if graph[u]:
            for v in graph[u]:
                self.DFS(graph, v, answer+[v], solution)
        else:
            solution.append(answer)


    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        if endWord not in wordList:
            return []
        if beginWord not in wordList:
            wordList.append(beginWord)
        graph = set(wordList)
        p = self.BFS(graph, beginWord, endWord)
        solution = []
        if not p:
            return solution
        color = {}
        for node in p:
            color.update({node: 1})
        self.DFS(p, endWord, [], solution)
        n = len(solution)
        for i in range(n):
            solution[i] = solution[i][::-1] + [endWord]
        return solution

beginWord = "hit"
endWord = "cog"
wordList = ['hot','hog',"cog"]
solution = Solution()
print(solution.findLadders(beginWord, endWord, wordList))
