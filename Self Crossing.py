class Solution(object):
    def isCross(self, edge1, edge2):
        if edge1[0] == edge2[0]:
            return False
        else:
            if (edge1[2]-edge2[1])*(edge1[3]-edge2[1]) <= 0 and (edge2[2] - edge1[1])*(edge2[3]-edge1[1]) <=0:
                return True
            else:
                return False

    def isSelfCrossing(self, x):
        """
        :type x: List[int]
        :rtype: bool
        """
        edges = []
        i = 0
        position = [0,0]
        for number in x:
            direction = i % 4
            if direction == 0:
                new_position = [position[0], position[1] + number]
                edge = [1,position[0],position[1],new_position[1]]
                if i == 3 and self.isCross(edges[0], edge):
                    return True
                elif i == 4 and self.isCross(edges[1], edge):
                    return True
                elif i > 4 and (self.isCross(edges[0], edge) or self.isCross(edges[2],edge)):
                    return True
                if i > 4:
                    edges.pop(0)
                edges.append(edge)
                position = new_position
            elif direction == 1:
                new_position = [position[0]-number, position[1]]
                edge = [0,position[1],position[0],new_position[0]]
                if i == 3 and self.isCross(edges[0], edge):
                    return True
                elif i == 4 and self.isCross(edges[1], edge):
                    return True
                elif i > 4 and (self.isCross(edges[0], edge) or self.isCross(edges[2],edge)):
                    return True
                if i > 4:
                    edges.pop(0)
                edges.append(edge)
                position = new_position
            elif direction == 2:
                new_position = [position[0], position[1]-number]
                edge = [1, position[0],position[1],new_position[1]]
                if i == 3 and self.isCross(edges[0], edge):
                    return True
                elif i == 4 and self.isCross(edges[1], edge):
                    return True
                elif i > 4 and (self.isCross(edges[0], edge) or self.isCross(edges[2],edge)):
                    return True
                if i > 4:
                    edges.pop(0)
                edges.append(edge)
                position = new_position
            else:
                new_position = [position[0]+number, position[1]]
                edge = [0, position[1], position[0], new_position[0]]
                if i == 3 and self.isCross(edges[0], edge):
                    return True
                elif i == 4 and self.isCross(edges[1], edge):
                    return True
                elif i > 4 and (self.isCross(edges[0], edge) or self.isCross(edges[2],edge)):
                    return True
                if i > 4:
                    edges.pop(0)
                edges.append(edge)
                position = new_position
            i += 1
        return False

solution = Solution()
x = [1,1,1,1]
print(solution.isSelfCrossing(x))
