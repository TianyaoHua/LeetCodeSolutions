class Solution(object):
    def dfs(self, visited, s, maxChoosableInteger,desiredTotal, dict):
        visited.sort()
        v_s = tuple(visited)
        if v_s in dict:
            return dict[v_s]
        for i in range(maxChoosableInteger, 0, -1):
            if i not in visited:
                if s + i >= desiredTotal:
                    dict.update({v_s: True})
                    return True
                elif not self.dfs(visited + [i], s+i, maxChoosableInteger, desiredTotal, dict):
                    dict.update({v_s: True})
                    return True
        dict.update({v_s: False})
        return False

    def canIWin(self, maxChoosableInteger, desiredTotal):
        """
        :type maxChoosableInteger: int
        :type desiredTotal: int
        :rtype: bool
        """
        dict = {}
        return self.dfs([],0,maxChoosableInteger,desiredTotal,dict)

print(Solution().canIWin(15,105))