# Definition for a point.
class Point(object):
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

class Solution(object):
    def line(self, point, points):
        h = {'undefine': 1}
        points.remove(point)
        for p in points:
            if point == p:
                for slope_key in h:
                    h[slope_key] += 1
            else:
                if point.x == p.x:
                    slope = float('inf')
                else:
                    slope = (point.y - p.y)/(point.x - p.x)
                if slope not in h:
                    h.update({slope: 1})
                h[slope] += 1
        return max(h.values())

    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        max_l = -float('inf')
        for point in points:
            max_l = max(max_l, self.line(point, points))
        return max_l

