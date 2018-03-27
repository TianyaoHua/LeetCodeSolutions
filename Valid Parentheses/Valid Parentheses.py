class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        table = {'(': 1, ')': -1, '{': 2, '}': -2, '[': 3, ']': -3}
        length = len(s)
        if length % 2 == 1:
            return False
        else:
            half_length = int(length / 2)
            center = 0
            while center < half_length:
                if table.get(s[center]) > 0 and table.get(s[center]) + table.get(s[center+1]) == 0:
                    bound = -1
                    for i in range(center-1,-1, -1):
                        if table.get(s[i]) < 0 or table.get(s[i]) + table.get(s[2*center + 1 - i]) != 0:
                            bound = i
                            break
                    s = s[0 : bound+1] + s[2 * center - bound+1 : ]
                    half_length = half_length-center+bound
                    center = 0
                else:
                    center += 1
        return not center


if __name__ == "__main__":
    solution = Solution()
    print (solution.isValid("(([]))"))
