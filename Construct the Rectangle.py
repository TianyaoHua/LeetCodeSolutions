class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        primfac = []
        d = 2
        while d * d <= area:
            while (area % d) == 0:
                primfac.append(d)  # supposing you want multiple factors repeated
                area //= d
            d += 1
        if area > 1:
            primfac.append(area)
        return primfac

print(Solution().constructRectangle(10000000))