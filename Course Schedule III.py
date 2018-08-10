class Solution(object):
    def core(self, courses, i, time, record):
        if(i, time) in record:
            return record[(i, time)]
        elif i >= len(courses):
            return 0
        else:
            while i < len(courses) and time+courses[i][0] - 1 > courses[i][1]:
                i += 1
            if i >= len(courses):
                return 0
            if (i == len(courses) - 1) or (courses[i][0] <= courses[i+1][0]):
                answer = 1 + self.core(courses, i+1, time+courses[i][0], record)
                record[(i, time)] = answer
                return answer
            else:
                answer1 = 1 + self.core(courses, i+1, time+courses[i][0], record)
                answer2 = self.core(courses, i+1, time, record)
                answer = max(answer1, answer2)
                record[(i, time)] = answer
                return answer

    def scheduleCourse(self, courses):
        """
        :type courses: List[List[int]]
        :rtype: int
        """
        courses.sort(key=lambda x: x[0])
        courses.sort(key=lambda x: x[1])
        return self.core(courses, 0, 1, {})

print(Solution().scheduleCourse([[5316,5539],[1968,5258],[4025,5081],[1300,7475],[1382,7434],[2277,3607],[821,2855],[797,5610]]))