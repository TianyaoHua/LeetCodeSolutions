class Solution(object):
    # def BFS(self, graph, s, t):
    #     Q = [s]
    #     d = {s: 0}
    #     color = {}
    #     for node in graph:
    #         color.update({node: 0})
    #     color[s] = 1
    #     while Q:
    #         u = Q.pop(0)
    #         for v in graph[u]:
    #             if color[v] == 0:
    #                 color[v] = 1
    #                 d[v] = d[u] + 1
    #                 Q.append(v)
    #     if t in d:
    #         return d[t]
    #     else:
    #         return -1
    #
    # def ladderLength(self, beginWord, endWord, wordList):
    #     """
    #     :type beginWord: str
    #     :type endWord: str
    #     :type wordList: List[str]
    #     :rtype: int
    #     """
    #     wordList.append(beginWord)
    #     # if endWord not in wordList:
    #     #     wordList.append(endWord)
    #     graph = {}
    #     n = len(wordList)
    #     for i in range(n):
    #         if wordList[i] not in graph:
    #             graph.update({wordList[i]:[]})
    #         for j in range(i+1, n):
    #             if self.edge(wordList[j], wordList[i]):
    #                 graph[wordList[i]].append(wordList[j])
    #                 if wordList[j] not in graph:
    #                     graph.update({wordList[j]: [wordList[i]]})
    #                 else:
    #                     graph[wordList[j]].append(wordList[i])
    #     print(graph)
    #     return self.BFS(graph, beginWord, endWord) + 1
    def BFS(self, graph, s, t):
        Q = [s]
        d = {s: 0}
        n = len(s)
        color = {}
        for node in graph:
            color.update({node: 1})
        color[s] = 0
        while Q:
            u = Q.pop(0)
            for i in range(n):
                for c in 'qwertyuiopasdfghjklzxcvbnm':
                    v = u[:i] + c + u[i+1:]
                    if v in graph and v!= u and color[v]:
                        d[v] = d[u] + 1
                        Q.append(v)
                        color[v] = 0
                        if v == t:
                            return d[v]
            color[u] = 0
        return -1

    def ladderLength(self, beginWord, endWord, wordList):
        if beginWord not in wordList:
            wordList.append(beginWord)
        #graph = {i: wordList[i] for i in range(len(wordList))}
        graph = set(wordList)
        return self.BFS(graph, beginWord, endWord)+1

solution = Solution()
beginWord = 'hot'
endWord = 'dog'
wordList = ["hot","cog","dog","tot","hog","hop","pot","dot"]
print(solution.ladderLength(beginWord, endWord, wordList))