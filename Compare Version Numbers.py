class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        version1 = version1.split('.')
        version2 = version2.split('.')
        n1 = len(version1)
        n2 = len(version2)
        i = n1-1
        while i > -1 and int(version1[i]) == 0:
            version1.pop()
            i -= 1
        i = n2-1
        while i > -1 and int(version2[i]) == 0:
            version2.pop()
            i -= 1
        n1 = len(version1)
        n2 = len(version2)
        flag = (n1>n2)*1 + (n1 == n2)*0 + (n1 < n2) * (-1)
        for i in range(min(n1, n2)):
            if int(version1[i]) > int(version2[i]):
                return 1
            elif int(version1[i]) < int(version2[i]):
                return -1
        return flag

solution = Solution()
version1 = "0"
version2 = "0"
print(solution.compareVersion(version1, version2))
