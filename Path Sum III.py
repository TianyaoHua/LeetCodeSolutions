class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
def stringToTreeNode(input):
    input = input.strip()
    input = input[1:-1]
    if not input:
        return None

    inputValues = [s.strip() for s in input.split(',')]
    root = TreeNode(int(inputValues[0]))
    nodeQueue = [root]
    front = 0
    index = 1
    while index < len(inputValues):
        node = nodeQueue[front]
        front = front + 1

        item = inputValues[index]
        index = index + 1
        if item != "null":
            leftNumber = int(item)
            node.left = TreeNode(leftNumber)
            nodeQueue.append(node.left)

        if index >= len(inputValues):
            break

        item = inputValues[index]
        index = index + 1
        if item != "null":
            rightNumber = int(item)
            node.right = TreeNode(rightNumber)
            nodeQueue.append(node.right)
    return root
def stringToInt(input):
    return int(input)
def intToString(input):
    if input is None:
        input = 0
    return str(input)
class Solution(object):
    def pathsum(self, node, sum, trigger, dict):
        if (node, sum, trigger) in dict:
            return dict[(node, sum, trigger)]
        elif not node:
            return 0
        else:
            if trigger == 0:
                answer = 0
                answer += self.pathsum(node.left, sum, 0, dict)
                answer += self.pathsum(node.right,sum, 0, dict)
                answer += self.pathsum(node.left, sum-node.val, 1, dict)
                answer += self.pathsum(node.right, sum-node.val, 1, dict)
            else:
                answer = 0
                answer += self.pathsum(node.left, sum-node.val, 1, dict)
                answer += self.pathsum(node.right, sum-node.val, 1, dict)
            answer += (sum == node.val)
            dict.update({(node, sum, trigger):answer})
            return answer

    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        dict = {}
        return self.pathsum(root, sum, 0, dict)


line = '[10,5,-3,3,2,null,11,3,-2,null,1]'
root = stringToTreeNode(line)

sum = 8

ret = Solution().pathSum(root, sum)

print(ret)