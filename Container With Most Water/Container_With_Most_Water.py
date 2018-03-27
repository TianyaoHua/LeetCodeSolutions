class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        start = 0
        end = len(height)-1
        previous_start = -1
        previous_end = end+1
        length = end-start
        max_Area = (height[start]>height[end])*height[end]*(length) + (height[start]<=height[end])*height[start]*(length)
        #while(start > previous_start or end < previous_end):
        while (end - start > 1):
            previous_start = start
            previous_end = end
            if height[start] <= height[end]:
                i = start+1
                while(height[i] < height[start] and i < end-1):
                    i += 1
                start = i;

                # for i in range(start + 1, end):
                #     if height[i] > height[start]:
                #         start = i
                #         break

            else:
                i = end-1
                while(height[i] < height[end] and i > start+1):
                    i -= 1
                end = i
                # for i in range(end - 1, start, -1):
                #     if height[i] > height[end]:
                #         end = i
                #         break
            #length = len(height)
            length = end - start
            temp_Area = (height[start]>height[end])*height[end]*(length) + (height[start]<=height[end])*height[start]*(length)
            max_Area = (temp_Area > max_Area)*temp_Area + (temp_Area <= max_Area)*max_Area
        return max_Area




if __name__ == "__main__":
    solute = Solution()
    answer = solute.maxArea([3,3,41,23,1,223,123,123,123])
    print(answer)
