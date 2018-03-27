class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        people.sort(key=lambda x:x[1])
        people.sort(key=lambda x:x[0],reverse=1)
        answer = []
        for person in people:
            answer.insert(person[1], person)
        return answer



solution = Solution()
print(solution.reconstructQueue([[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]))