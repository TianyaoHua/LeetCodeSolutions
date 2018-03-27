class Solution(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        if not preorder:
            return True
        preorder = preorder.split(',')
        stack = [[preorder[0], 2]]
        for c in preorder[1:]:
            if not stack:
                return False
            else:
                stack[-1][1] -= 1
                if stack[-1][1] == 0:
                    stack.pop()
                if c != '#':
                    stack.append([c, 2])
        return not bool(stack)

solution = Solution()
preorder = "9"
print(solution.isValidSerialization(preorder))
