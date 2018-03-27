class Solution(object):
    def interval(self, intervals):
        intervals.sort(key=lambda x: x[1], reverse=1)
        intervals.sort(key=lambda x: x[2], reverse=1)
        intervals.sort(key=lambda x: x[0])

        left_interval = intervals[0]
        left_point = left_interval[0]
        right_interval = intervals[0]
        right_point = left_interval[1]
        out_lines = []
        out_points = []
        left_flag = []
        for i in range(len(intervals)):
            if intervals[i][0] <= right_point < intervals[i][1]:
                right_point = intervals[i][1]
                right_interval = intervals[i]
            elif intervals[i][0] > right_point:
                out_lines.append(left_interval)
                left_flag.append(1)
                out_points.append(left_point)
                out_points.append(right_point)
                if right_interval != left_interval:
                    out_lines.append(right_interval)
                    left_flag.append(0)
                left_interval = intervals[i]
                left_point = left_interval[0]
                right_interval = intervals[i]
                right_point = left_interval[1]
        out_lines.append(left_interval)
        left_flag.append(1)
        out_points.append(left_point)
        out_points.append(right_point)
        if right_interval != left_interval:
            out_lines.append(right_interval)
            left_flag.append(0)
        return out_lines, out_points,left_flag

    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        buildings.sort(key= lambda x: x[2], reverse= 1)
        i = 0
        n = len(buildings)
        height_level = buildings[0][2]
        intervals = []
        answer = []
        while i < n:
            j = i
            while j < n and buildings[j][2] == height_level:
                j += 1
            outlines, outpoints, left_flag = self.interval(buildings[i:j] + intervals)
            for i in range(len(outlines)):
                if outlines[i][2] == height_level:
                    if left_flag[i]:
                        answer.append([outlines[i][0], height_level])
                        answer.sort(key=lambda x: x[0])
                    elif not (answer and height_level == answer[-1][1]):
                        answer.append([outlines[i-1][1], height_level])
                        answer.sort(key=lambda x: x[0])
            i = j
            if i < n:
                height_level = buildings[i][2]
                intervals = []
                for k in range(0, len(outpoints), 2):
                    intervals.append([outpoints[k], outpoints[k+1], height_level+1])
        for k in range(1, len(outpoints), 2):
            answer.append([outpoints[k], 0])
        return answer

solution = Solution()
buildings =[[0,2,1],[1,4,2],[3,5,1]]
print(solution.getSkyline(buildings))