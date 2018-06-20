class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        absence = 0
        late = 0
        for i in range(len(s)):
            absence += s[i] == 'A'
            if s[i] == 'L':
                late += 1
            else:
                late = 0
            if absence > 1 or late > 2:
                return False
        return True