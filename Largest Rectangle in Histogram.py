class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        n = len(heights)
        left = [i for i in range(n)]
        right = [i+1 for i in range(n)]
        for i in range(1, n):
            j = i-1
            while j >= 0 and heights[i] <= heights[j]:
                j = min(left[j], j-1)
            left[i] = j+1
        for i in range(n-2,-1,-1):
            j = i+1
            while j < n and heights[i] <= heights[j]:
                j = max(right[j], j+1)
            right[i] = j
        max_area = 0
        for i in range(0, n):
            area = heights[i]*(right[i]-left[i])
            if area > max_area:
                max_area = area
        return max_area

solution = Solution()
heights = [4,2,0,3,2,4,3,4]
print(solution.largestRectangleArea(heights))

