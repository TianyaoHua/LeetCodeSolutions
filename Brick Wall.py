class Solution:
    def leastBricks(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        """
        h = {}
        s = 0
        for layer in wall:
            s = 0
            for brick in layer[0:-1]:
                s += brick
                if s not in h:
                    h[s] = 0
                h[s] += 1
        return len(wall) - max(h.values())


print(Solution().leastBricks([[1],[1],[1]]))