class Solution(object):
    def volume(self, height, p, r):
        v = 0
        if height[p] < height[r]:
            height_base = height[p]
            i = p+1
            while height_base - height[i] >= 0 and i < r:
                v += height_base-height[i]
                i += 1
        else:
            height_base = height[r]
            i = r-1
            while height_base - height[i] >= 0 and i > p:
                v += height_base - height[i]
                i -= 1
        return v

    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        v = 0
        n = len(height)
        height = [0] + height +[0]
        walls = []
        for i in range(1, n+1):
            if height[i-1] <= height[i] and height[i] >= height[i+1]:
                walls.append(i)

        k = 0
        n_walls = len(walls)
        find_higher = 0
        while k < n_walls - 1:
            j = k
            j_max = j+1
            while j < n_walls-1:
                j += 1
                if height[walls[j]] >= height[walls[j_max]]:
                    j_max = j
                if height[walls[j]] >= height[walls[k]]:
                    v += self.volume(height, walls[k], walls[j])
                    k = j
                    find_higher = 1
                    break
            if find_higher:
                find_higher = 0
            else:
                v += self.volume(height, walls[k], walls[j_max])
                k = j_max
        return v

if __name__ == "__main__":
    solution = Solution()
    answer = solution.trap([9,6,8,8,5,6,3])
    print(answer)