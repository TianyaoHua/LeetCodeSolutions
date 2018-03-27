import itertools
class Solution(object):
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        n = len(points)
        distances = [[0 for i in range(n)] for j in range(n)]
        distances_hash = {}
        for i in range(n):
            for j in range(i+1,n):
                distance = (points[i][0]-points[j][0])**2+(points[i][1]-points[j][1])**2
                distances[i][j] = distance
                distances[j][i] = distance
                if distance not in distances_hash:
                    distances_hash.update({distance:[]})
                distances_hash[distance].append((i,j))
        answer = 0
        for distance in distances_hash:
            n = len(distances_hash[distance])
            for i in range(n):
                edge1 = distances_hash[distance][i]
                for j in range(i+1, n):
                    edge2 = distances_hash[distance][j]
                    if edge1[0]==edge2[0]:
                        answer += 2
                        if distances[edge1[1]][edge2[1]] == distance:
                            answer += 4
                    if edge1[0] == edge2[1]:
                        answer += 2
                        if distances[edge1[1]][edge2[0]] == distance:
                            answer += 4
                    if edge1[1] == edge2[0]:
                        answer += 2
                        if distances[edge1[0]][edge2[1]] == distance:
                            answer += 4
                    if edge1[1] == edge2[1]:
                        answer += 2
                        if distances[edge1[0]][edge2[0]] == distance:
                            answer += 4
        return answer
print(Solution().numberOfBoomerangs(
[[0,0],[1,0],[-1,0],[0,1],[0,-1]]))
