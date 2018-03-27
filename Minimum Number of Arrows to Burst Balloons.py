class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        points.sort(key=lambda x:x[0])
        answer = 0
        n = len(points)
        i = 0
        overlap = [-float('inf'), float('inf')]
        while i < n:
            p_overlap = [max(overlap[0], points[i][0]), min(overlap[1], points[i][1])]
            if p_overlap[1] >= p_overlap[0]:
                overlap = p_overlap[:]
                i += 1
            else:
                overlap = [-float('inf'), float('inf')]
                answer += 1
        return answer+1

print(Solution().findMinArrowShots([[1,2],[3,4]]))
