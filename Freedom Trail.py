class Solution(object):
    def dfs(self, m, key, index, i, j, dict):
        if (i,j) in dict:
            return dict[(i, j)]
        elif j >= len(key):
            return 0
        else:
            steps = float('inf')
            for u in index[key[j]]:
                rotate = min(abs(u-i), m-abs(u-i))
                press = 1
                steps = min(steps, rotate+press+self.dfs(m, key, index, u, j+1, dict))
            dict[(i,j)] = steps
            return steps

    def findRotateSteps(self, ring, key):
        """
        :type ring: str
        :type key: str
        :rtype: int
        """
        index = {}
        n = len(ring)
        m = len(ring)
        for i in range(n):
            if ring[i] not in index:
                index[ring[i]] = []
            index[ring[i]].append(i)
        dict = {}
        return self.dfs(m,key,index,0,0,dict)

print(Solution().findRotateSteps("godding","godding"))