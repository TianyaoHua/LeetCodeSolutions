class Solution(object):
    def count(self, nums, i, j, lower, upper):
        if j - i > 0:
            n = j - i + 1
            p = (i+j)//2
            dict_left = {}
            dict_right = {}
            s_left = 0
            answer = 0
            for k in range(p, i-1,-1):
                s_left += nums[k]
                if s_left not in dict_left:
                    dict_left.update({s_left: 0})
                dict_left[s_left] += 1
            s_right = 0
            for k in range(p+1, j+1):
                s_right += nums[k]
                if s_right not in dict_right:
                    dict_right.update({s_right:0})
                dict_right[s_right] += 1
            if n//2 > upper-lower+1:
                for key in dict_left:
                    for target in range(lower, upper+1):
                        if target-key in dict_right:
                            answer += dict_left[key]*dict_right[target-key]
                return answer + self.count(nums, i, p,lower,upper)+self.count(nums,p+1,j,lower,upper)
            else:
                for key_left in dict_left:
                    for key_right in dict_right:
                        if lower <= key_left+key_right <= upper:
                            answer += dict_left[key_left]*dict_right[key_right]
                return answer + self.count(nums, i, p,lower,upper)+self.count(nums,p+1,j,lower,upper)
        else:
            return int(lower <= nums[i] <= upper)


    def countRangeSum(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """
        lower = int(lower)
        upper = int(upper)
        answer = self.count(nums,0,len(nums)-1,lower,upper)
        return answer

solution = Solution()
nums = [-24,-16,-15,14,14,17,-26,-1,-11,4,2,-5,-1,23,19,-23,-20,-18,5,23,24,-21,13,10,19,-25,-11,12,15,12,-23,22,14,22,-25,-19,11,19,-13,-5,10,15,-19,14,24,21,15,-10,17,-2,-12,-19,-11,-12,27,21,23,2,-26,-11,17,-5,7,-28,2,12,-20,27,-11,-20,-13,10,-30,-25,-15,-17,15,15,3,10,-15,-5,-28,-11,-9,21,2,-20,-1,-4,-11,-6,20,-1,-14,28,27,14,12,-23,22,-2,-18,15,16,20,-29,24,-22,-17,24,22,12,18,24,-13,0,2,-22,-4,0,-4,-23,-23,-25,-7,20,-15,-27,-29,14,-12,4,-21,-21,10,-16,-15,-22,-10,-25,-18,-20,-3,19,-17,21,-10,-24,-8,11,28,-27,24,-26,-1,-5,-1,12,-1,13,24,2,14,20,-6,-24,-20,15,11,-16,-30,12,-19,16,8,25,29,18,28,-3,-23,5,9,-18,9,10,-8,1,-1,-18,-9,-10,-15,-2,4,-2,-24,-8,-11,0,-18,17,-2,15,-5,0,-30,-22,29,0,11,17,-13,-16,10,0,-22,-30,28,-2,-16,13,0,-24,13,-25,-10,14,-25,27,15,7,25,6,23,28,12,-7,-24,-22,-25,-13,1,21,-15,-20,-1,18,-15,16,-5,-23,-10,-5,7,-20,1,7,-9,3,-24,21,-15,16,9,-6,5,29,-28,25,-27,22,-22,-22,-24,17,-13,21,-27,12,-5,16,-27,-16,17,-29,-13,-24,-8,18,13,-22,12,-6,4,-20,-3,26,-5,-28,20,14,13,-27,-17,-19,17,-12,-7,3,24,6,11,17,26,1,-10,9,-15,-5,24,-25,3,27,26,-6,-2,26,-13,10,27,2,22,-10,-3,19,-11,-3,-20,16,-16,2,10,29,6,16,-18,-30,19,9,-12,14,-30,-1,-24,14,-10,-27,-17,26,-11,21,16,15,-28,27,-4,12,-11,-3,5,-13,-6,6,21,-24,4,-8,28,-5,-26,-13,-28,-18,-3,-15,6,-5,-16,20,5,1,-21,27,21,11,-27,-21,-30,-27,7,7,16,26,17,-21,-3,15,12,18,-18,-14,-14,19,10,-12,-9,-26,15,9,4,-27,11,18,-18,-19,28,-7,4,-4,-4,-23,-25,-12,29,13,0,-15,-11,6,-5,21,-26,13,15,-3,-3,24,-11,17,8,-27,-17,13,-14,1,6,-29,23,14,-20,4,6,-12,12,-2,-8,-5,11,20,29,-18,13,18,-15,-27,-3,-19,5,20,14,15,5,-21,-17,0,24,-30,15,4,-1,-2,10,-11,-14,-29,-9,17,12,-18,14,17,-18,-30,13,9,-1,-22,20,-21,3,-14,28,28,18,-9,14,26,-27,10,-16,-19,4,9,-17,29,-29,-19,-29,-4,-13,24,2,14,-1,2,13,4,17,-24,5,11,15,9,12,-1,19,-24,-29,0,0,12,2,-3,-6,-29,0,2,-2,-10,29,-16,-5,26,21,24,-7,27,6,-6,-15,-6,11,-26,-25,29,-27,20,8,4,-22,-12,-11,-24,-20,0,-23,7,24,-25,1,23,29,-28,-7,-9,1,11,-9,0,-1,-7,7,25,5,-18,-6,3,17,-8,-23,5,-1,-25,13,3,7,8,-11,-18,11,-1,0,-26,27,-27,26,9,29,-20,9,13,-30,-19,1,-15,5,-28,17,10,-7,11,2,-9,11,2,7,-8,19,15,-26,28,-7,-4,-11,25,26,2,28,-10,9,13,16,-13,-9,3,6,-30,-1,-24,26,2,-12,-12,14,-24,-24,-29,-5,11,-24,-7,-28,-23,-6,9,-17,-20,-1,16,16,11,-27,24,-1,-28,7,23,-6,24,-15,11,25,-13,-9,3,-25,-30,16,28,26,-16,25,3,-10,-20,26,22,-29,-7,29,18,-22,-8,1,-17,19,10,22,-24,8,6,24,27,16,10,10,21,-5,-25,22,7,-1,-24,19,-16,-26,-22,-22,11,-9,26,-7,5,-19,28,-15,-12,15,9,-12,3,-10,-27,-3,25,-14,-22,4,-18,27,-19,6,5,-13,-2,25,-19,6,7,-8,0,23,-30,-25,-8,-13,0,-22,-7,-25,15,-12,3,-18,-19,23,-26,-8,3,-14,-7,-8,16,-8,-5,5,14,24,-19,7,-5,14,20,29,-18,-30,4,7,-11,-21,24,4,6,-25,-3,25,-22,-18,12,-8,-30,-24,-21,-4,14,4,-24,-18,0,-4,-15,18,-10,-21,-3,0,28,-5,25,8,-24,28,15,-19,5,-15,0,27,11,-10,-7,-10,10,-14,23,-16,1,3,15,4,9,-24,13,17,-1,23,26,-23,-26,2,-6,-4,-4,25,0,-5,-3,1,9,8,-11,27,-21,-23,19,19,6,-16,18,0,10,-30,-28,-27,20,-11,-1,-17,-25,22,-20,18,15,-19,-28,26,-27,5,24,20,-9,12,17,1,16,-7,-7,-1,27,7,29,22,27,25,-6,-9,-10,10,-2,-19,-28,-17,-12,-20,-14,-3,-9,-13,-16,-29,16,29,-21,-25,-16,-27,-2,18,-3,8,3,11,18,27,-16,-24,-11,10,13,-24,16,-25,-19,-13,16,-16,24,18,-2,-23,-20,-6,-3,18,-24,-23,-27,-11,23,-6,26,-24,1,3,-8,-2,-16,4,23,29,-6,26,-28,-13,-9,-14,-21,-3,15,9,-27,23,-15,1,-11,17,27,-18,-14,19,1,2,-24,7,22,-6,-28,-12,23,-17,7,28,-1,18,-24,11,8,-16,25,4,-1,-30,-9,28,-14,-23,-22,26,-12,-23,-4,-26,-30,12,24,11,-14,6,18,-13,-12,-28,22,17,-28,-22,-30,-14,21,15,23,21,15,9,-10,10,25,-11,11,-2,1,-4,11,-6,-27,3,12,-10,24,5,26,5,13,0,-21,18,24,28,-26,-19,-6,-24,-28,7,20,2,-20,21,5,-15,25,17,13,-19,-13,-16,-23,0,-30,-8,-4,-4,-13,-8,-23,-10,-10,-13,-16,-10,-2,6,-29,-7,0,-13,29,-24,10,11,-14,-30,-30,-17,-6,-14,-8,-22,12,-14,6,10,-29,16,3,-22,-8,-13,-1,2,-25,18,28,-9,-15,-11,8,-11,-29,-27,-5,-11,-24,-13,-24,-13,-19,-7,-19,-10,29,9,3,24,5,27,24,-22,-6,22,-21,17,18,10,10,6,10,9,15,-28,13,-13,-23,-28,-25,-19,23,-26,21,7,11,-5,-4,22,-8,-14,-15,18,-13,-19,19,15,8,-12,20,-5,29,-27,11,8,-19,-3,28,8,-6,15,23,23,-23,19,26,-8,-30,1,17,-19,-12,19,-9,-19,19,5,27,27,-3,-4,-18,-15,20,-29,-27,-9,2,-17,23,2,7,26,-8,-22,4,7,1,0,5,-20,3,0,0,0,-15,3,18,3,10,5,-17,21,4,4,-14,-24,14,28,-21,-28,-17,-30,-28,17,6,-16,-25,-30,-30,3,18,-28,4,17,14,13,-4,22,-30,-28,0,-6,-12,-9,29,16,26,1,23,2,27,-2,-16,-3,5,-28,13,-24,22,-21,4,-7,23,-7,23,-4,-7,13,26,1,0,19,-27,-15,-5,-19,-23,28,-19,-16,25,6,-30,21,-3,9,-7,-17,25,-5,18,-21,28,-27,-27,-24,-24,-16,25,-27,27,-17,4,4,-19,-22,-12,28,29,-22,27,-29,22,19,-4,14,-18,-21,-23,23,10,-20,-26,-14,-7,1,16,-16,7,9,15,-16,-1,-26,9,23,-8,-26,-12,0,5,24,-20,1,28,-14,-14,-27,-8,26,5,-21,12,-8,14,15,-12,-29,3,9,-16,-28,6,11,-24,20,21,4,6,16,-26,0,4,-8,7,14,17,5,-1,-10,19,20,-3,-17,-29,-27,23,-28,12,1,-12,-21,19,8,-30,-10,-19,2,18,28,-25,-15,2,-11,-18,-24,5,-22,27,-21,-5,12,18,-16,-28,-21,-5,-22,-29,-30,-22,13,-27,-26,20,22,24,-19,-28,24,13,-7,28,0,-4,-22,16,21,-30,29,-24,29,-29,-8,-14,22,28,-21,13,-16,24,-20,14,-16,-18,-26,11,-7,-30,7,25,2,10,29,19,-23,25,13,6,28,-30,20,-14,-26,22,-27,-18,25,-9,-21,-13,-6,14,-12,-5,-6,-7,16,-19,9,6,1,1,0,0,-1,21,13,0,-25,-13,-21,12,-11,12,-17,16,-4,11,-14,26,16,-22,5,19,10,-7,-21,-27,2,-8,27,4,-18,15,14,24,19,-6,-9,21,-13,-24,-9,26,10,-23,-17,-18,-15,0,-30,-20,24,14,-16,13,-16,25,-13,-23,-22,21,-18,14,11,-16,4,-2,13,-5,12,21,-1,28,-13,-26,26,11,18,14,16,26,15,-9,-3,-4,23,-21,24,-21,-18,26,7,12,-17,-6,-4,-20,-10,-30,6,-2,7,-30,8,-12,25,13,9,1,-7,-26,20,16,-18,13,2,-22,15,22,-18,-14,-28,20,5,-22,-7,27,9,2,7,16,-8,-3,-27,-10,13,15,-4,-22,15,-21,-9,22,17,-25,15,-9,7,-2,27,29,-12,6,-20,14,9,-3,28,14,17,10,29,-9,-11,-18,-24,-23,-5,-10,11,23,20,-11,-27,24,-15,6,26,-3,-24,2,-20,-4,20,16,-4,9,-27,-26,-3,-11,-12,-30,-18,-8,-4,-14,-25,-30,6,21,28,14,9,22,-14,10,6,-30,-5,18,-18,28,5,-9,-6,28,10,6,3,10,-9,14,-24,11,3,-13,13,22,-13,-16,6,-25,21,20,25,20,-14,15,-15,26,-10,20,3,14,26,-17,23,-23,-24,6,-11,-21,19,-11,19,-21,8,-28,12,-28,-5,10,-10,8,28,5,-29,-6,-6,16,-3,-21,14,-11,21,18,12,-18,-21,12,-4,20,25,-26,-28,16,-6,-10,-14,-10,-3,2,8,29,11,-3,-13,9,-27,12,-15,-17,7,25,-7,2,-1,-2,-14,3,-26,-24,27,-25,10,-8,-22,5,12,7,-25,19,-3,-1,28,-1,20,-3,-9,-29,23,-10,8,10,19,-1,29,-6,17,-4,-11,-21,19,-10,-19,-26,-11,23,-6,15,-6,-5,4,-11,-17,-2,22,-5,26,-3,12,24,-1,-16,-30,-19,-4,13,-24,-25,11,14,20,-24,15,-3,-10,2,-24,9,-13,-17,-4,-7,8,29,-14,25,-17,21,5,-23,18,8,-14,2,20,-22,-13,24,12,-29,-2,-30,-29,13,-22,26,-18,11,-28,-16,-14,-29,-15,-14,21,22,28,-5,18,-30,-28,4,-23,7,1,20,4,27,-20,-12,-14,-9,-12,-21,3,-26,-17,-24,-11,4,6,-22,18,9,-14,14,18,-26,16,23,-8,21,20,-13,-24,24,-29,-6,-27,7,18,24,18,-25,-21,29,27,-8,-25,-4,18,15,21,22,3,21,-1,-16,-22,-5,-29,-29,24,-10,-7,-19,17,-4,-12,-28,4,-2,26,-7,12,6,-26,27,12,-7,17,-6,-1,-6,17,-13,-10,1,-29,-12,-25,-2,-17,-6,10,-14,18,27,-9,7,-28,-13,7,-3,28,10,-8,-26,21,-5,-3,11,6,21,-5,6,2,-17,-18,11,-13,-29,-25,23,-22,8,23,15,4,-12,5,13,3,-7,14,27,-1,4,22,21,4,-8,10,-14,-6,1,-15,-2,-19,1,28,22,-17,4,-29,-7,-10,-16,-10,-13,19,25,-8,-10,29,7,-12,-28,4,10,-14,24,-13,26,-4,25,-27,-9,2,-16,0,20,27,-22,-2,-8,-9,-23,-3,0,-5,2,-6,-27,13,21,19,-7,-19,-27,-29,-15,11,26,7,21,26,-24,-22,19,14,26,9,10,-16,0,-15,-29,4,16,-30,-1,27,10,2,-11,14,-17,-20,-8,-30,-7,-5,4,23,-27,10,9,-19,11,-6,-8,26,9,6,26,22,-13,15,-12,20,-17,-6,29,-6,29,3,-8,-20,-16,-1,18,14,-8,-15,-8,28,27,-26,2,16,-30,-8,10,28,9,25,-8,-3,-29,18,0,-21,9,27,26,-5,26,4,-5,-29,0,-29,8,21,6,28,24,24,-27,6,28,-16,-30,21,-6,-19,26,17,24,14,-27,-21,-6,-13,16,-6,22,22,-26,22,-7,3,-5,-11,-9,20,-4,26,29,1,-29,22,19,-5,-30,29,12,-16,7,11,-2,-24,15,-7,-17,23,22,-20,-27,7,-8,29,-13,28,12,26,-23,7,-7,-16,-13,-12,-23,6,-17,12,-9,-9,7,27,-19,-19,-19,-21,-16,-14,18,27,13,8,3,11,-8,8,-3,29,-16,19,23,24,1,25,1,9,-22,-5,12,16,11,-12,8,13,24,-23,15,12,-15,-25,4,14,-22,6,24,-26,14,16,-18,-4,-29,2,-22,9,-28,-5,-25,20,-13,-5,14,2,-16,-4,14,-23,-4,29,-17,23,20,16,-12,-15,0,-26,24,11,14,-20,2,-28,8,17,-4,-14,11,19,26,-15,8,12,29,-13,-11,3,-22,13,1,7,-3,22,-21,4,-5,17,24,-8,-8,-6,9,-22,-2,-20,25,-5,27,-30,21,25,-10,0,-23,-3,5,9,3,-16,-17,-21,18,-2,1,-21,-15,8,-12,-8,-9,9,-10,23,-26,-29,-6,25,-16,-4,-18,-23,-22,-16,-30,16,-22,6,22,-21,25,-1,2,17,-28,3,-28,-6,-21,3,0,-21,18,23,-25,-5,18,-22,-11,-20,-6,8,-16,-12,-25,25,-2,7,-10,19,4,-2,-17,14,27,9,11,-12,-20,-26,-5,18,10,26,24,-12,-5,6,-28,-7,-12,15,-9,24,-1,26,15,23,-20,27,-14,25,0,9,9,-5,29,8,-6,-14,6,7,-12,-23,-29,-19,-28,23,-25,-1,-20,21,-22,11,-10,18,5,4,18,23,13,-10,-30,-18,0,1,20,-30,-20,-18,27,14,-22,2,-10,-4,-29,-4,25,28,1,-22,-22,5,-24,-12,13,24,24,-23,-11,5,24,22,-27,-4,-15,5,-9,1,25,-29,-20,-9,-20,2,26,-18,5,23,-24,19,-30,-8,26,-13,-23,2,22,-15,-21,25,10,20,-10,4,13,2,24,21,-2,2,16,-29,-6,1,20,28,15,-9,-7,17,9,-19,23,12,-23,20,18,-20,-10,25,26,-11,15,25,-30,21,16,19,19,-30,17,9,0,5,21,-4,-13,23,-27,29,-8,24,23,-12,14,26,-30,11,18,-24,-12,-4,-8,0,24,-16,25,23,3,-30,20,-21,25,4,29,-29,0,0,-13,-9,20,-26,-2,7,12,10,4,7,-18,18,26,5,-10,-1,15,19,-1,9,18,-10,-18,-20,-11,17,-23,17,12,19,13,18,9,5,-7,23,18,9,2,14,-22,2,-13,-2,-27,-26,-14,24,6,-7,22,11,-17,-4,20,14,19,19,-15,16,-27,7,26,28,22,20,-21,19,21,23,-10,8,-18,-16,-5,14,-24,24,9,-15,-11,-30,-4,18,4,0,-13,13,-25,-27,10,-30,27,21,20,-4,-24,29,-6,23,14,29,24,-12,-18,-16,13,-21,-9,8,15,9,-12,-29,2,24,10,14,-7,8,8,-16,-17,-1,27,-25,7,21,-15,-1,-17,-1,-7,23,-13,-6,-8,-17,-6,9,-23,-8,-25,20,-9,11,-30,27,-27,17,15,-29,-3,15,-4,-25,-12,-13,-22,-1,11,14,1,14,24,18,16,-9,-30,-21,-19,-20,10,1,-5,14,22,19,-26,24,20,27,-12,2,24,19,-19,21,3,26,18,18,-24,23,-8,25,12,15,-13,1,-25,-9,10,-21,-13,11,25,-9,-11,18,22,-10,-17,-10,-2,-23,27,3,3,14,-25,-16,15,27,26,-7,-8,8,-8,-7,28,-30,-22,29,-19,-14,28,26,14,8,24,-12,16,22,-17,-1,7,0,-12,-9,5,22,17,-7,17,4,-13,5,18,14,-18,-1,-17,21,29,-15,-29,-1,12,-10,14,-9,-5,-18,-18,24,-24,-25,-20,-8,14,20,27,-28,12,-24,12,-1,21,-14,29,16,-14,-15,-29,18,-29,-21,-29,28,-5,7,8,-6,-6,-29,-17,15,-15,8,13,-5,-20,-3,22,1,17,-25,-21,11,2,-19,9,22,5,6,9,-10,-5,16,-19,29,2,4,-23,-4,13,24,27,20,11,-17,25,27,-16,3,-15,0,20,13,-1,8,-12,24,-17,11,10,-16,-11,27,3,-25,-15,24,17,11,-27,-27,4,12,19,7,5,20,10,19,9,29,12,-2,24,1,28,22,5,-6,-19,-4,2,9,15,-29,-18,1,-28,-9,15,2,24,-3,-25,24,2,-9,-17,-26,14,7,-9,-21,3,7,5,9,14,9,20,-28,-30,-11,1,-6,7,-8,20,29,-7,-26,21,27,22,-11,-13,-21,-20,-15,19,-13,14,12,6,-26,-25,-25,-16,19,-20,2,9,-24,11,9,-14,-1,4,-28,1,-28,25,-5,-14,-4,2,15,-14,1,-14,-12,-13,26,10,24,10,-23,15,-15,-7,8,24,15,-25,-14,22,25,1,-12,19,-2,-7,25,-14,-16,-25,2,-7,-27,21,-10,19,-14,27,-18,29,5,15,-19,3,18,23,-12,0,-6,12,17,-3,25,19,-23,-8,6,28,-8,-30,25,-20,9,-21,-22,21,4,23,25,16,5,-16,-22,0,29,20,5,22,-13,1,-18,15,1,19,-4,-24,26,3,13,-26,26,8,24,-25,-7,-4,22,-8,-24,-30,-23,-23,21,-5,-29,-5,10,8,3,15,-11,26,3,-8,-21,-19,-9,-1,-5,-25,21,11,10,-15,-13,-25,-2,-25,9,-5,16,-27,-13,-17,-13,-18,16,27,6,5,-28,6,26,-15,-27,23,26,29,5,-11,8,5,-4,-1,25,19,-26,-30,12,18,11,3,3,-1,-29,5,-5,13,-27,-7,-20,-9,7,2,-6,0,-3,-12,11,6,-24,17,0,-23,17,-30,-2,24,10,28,19,-9,13,-22,-22,28,-15,-28,25,-5,-10,7,-26,4,-26,24,13,-16,21,23,28,8,29,-24,-19,-17,-24,16,5,24,-29,-30,-2,-21,25,-18,20,-4,0,-8,9,17,24,-22,24,26,-22,27,10,28,27,24,0,16,19,5,-3,-29,21,17,27,-19,-23,28,23,-7,-23,1,-10,-28,-27,24,-25,-5,-26,6,-30,17,2,20,27,2,26,11,29,-11,-24,9,-26,-12,28,13,23,29,15,-15,-20,-17,8,-19,-17,-21,7,-3,23,9,-13,11,-7,15,-4,-25,6,0,-2,-4,27,-25,-27,-1,18,3,10,8,26,19,2,-15,-30,27,14,-4,-9,5,-16,-6,-27,11,14,1,-28,-2,0,-26,-4,-5,-29,-29,-14,-9,-10,4,14,12,17,-30,-9,4,-30,-18,26,14,-24,24,-29,3,-19,-9,20,8,-28,12,16,1,20,24,-11,-5,-6,-8,11,-1,-18,24,14,23,-13,28,-6,14,10,-19,6,-12,-24,-5,6,8,-7,-23,10,-3,2,-23,20,-8,-22,15,14,-20,1,3,-22,-3,-23,13,-26,-21,-17,20,16,-9,27,-8,-13,12,4,-1,13,-28,-18,-20,-23,10,-7,6,-7,-8,-18,7,29,21,10,-16,-19,-19,9,22,-6,-26,-15,27,-20,-13,28,-25,1,-4,18,-5,-1,-28,-7,15,-25,-1,23,12,-26,0,-22,-15,26,12,-8,3,-21,-15,-4,5,18,6,29,-14,-21,4,-22,-15,-4,-22,16,-9,4,6,29,-5,6,11,-30,-20,-25,-8,8,5,-13,-13,11,-15,-27,19,-29,-26,-15,19,-28,27,-24,0,-11,15,-17,-29,1,6,-27,-20,3,19,23,15,-7,-16,1,0,28,-26,3,-6,11,24,21,-18,1,7,9,-13,-12,-29,-28,-30,21,21,-12,14,13,22,1,-6,-21,-20,10,-21,0,13,-17,-27,8,20,-6,3,0,5,15,-29,-1,-7,-16,-8,15,3,-18,6,-15,-23,-22,5,-19,-26,16,14,-11,22,-21,19,23,-4,-6,18,6,20,27,28,26,-7,13,-16,-23,-14,8,-20,16,-11,-22,1,-3,22,0,22,11,-2,-25,26,0,-12,6,7,3,7,-19,-21,-18,10,-8,-22,-14,14,10,-21,26,6,-21,-4,-1,-25,-27,26,-29,14,16,-22,21,22,2,17,-20,-18,2,-2,-22,-4,-8,-7,-30,17,-9,-11,-21,-7,-25,8,-28,-4,-26,-9,20,-13,10,9,25,21,24,25,-30,18,24,-28,-29,-27,21,29,-10,-23,20,-17,-16,-18,17,-15,17,-1,-26,1,28,-23,21,-16,-1,27,-19,-13,24,-24,-19,-2,-18,-15,25,-11,7,-24,-6,-12,-14,-4,-12,21,8,-8,10,1,4,14,23,24,-3,16,-16,6,29,21,-1,11,-9,-21,-13,-21,-23,29,22,-18,0,12,-8,-29,26,16,-3,8,7,20,10,-9,0,28,-20,28,1,-10,-13,-10,-16,19,-21,1,-25,29,-14,26,3,1,2,-25,28,-7,25,-27,14,4,22,-26,13,-27,-7,29,29,-17,-4,-2,28,2,10,20,2,-12,6,25,-12,14,-26,-16,-19,9,-23,10,-27,-18,19,19,11,-22,-9,17,26,8,-5,19,12,13,24,8,-20,25,13,-24,-10,11,7,-4,21,-29,7,0,-11,26,-8,-27,11,-28,15,-27,-13,1,-3,-8,-27,-16,0,27,-20,28,26,0,-29,-14,8,9,4,-14,3,20,-9,-24,-3,-12,9,18,-10,-5,-8,-22,-19,11,-20,20,-9,12,-13,6,4,7,-8,14,18,-6,-7,-30,14,20,-19,20,-15,-4,-22,-28,-21,-22,-16,22,4,-12,-18,-4,13,9,-3,13,-2,-12,-17,-2,2,21,-18,10,-17,-24,0,-23,21,-23,11,-3,1,25,-15,8,23,-17,-6,-14,17,29,-15,-12,23,-6,-22,7,-3,-8,-13,19,-12,27,-30,3,-19,-8,-18,22,-13,-12,8,-27,-12,-3,-19,-5,-5,7,-5,10,-11,13,27,15,3,3,23,-14,4,-4,-12,-11,20,-19,-30,7,25,-27,3,13,-27,-8,-22,-5,29,23,-30,-6,25,6,8,6,13,-20,-18,28,29,-8,-8,-22,8,1,29,13,8,-27,27,-3,-18,23,-20,27,27,-13,27,-23,-4,3,-9,-20,-5,23,-5,-17,5,-9,6,-16,20,-23,2,-13,-12,10,-8,11,-6,-27,-6,29,-16,-21,-27,8,-11,-5,-14,-30,22,2,9,-30,2,19,6,-25,-21,5,-15,6,22,17,-13,-8,-7,-25,2,-2,-29,-26,-6,-30,-16,20,-10,-21,-29,-27,-25,-2,7,19,20,-13,-2,-18,-8,-25,1,-10,0,-28,-3,14,-11,19,-10,17,18,-6,19,24,-25,6,1,6,-14,4,13,-8,27,-15,-14,-26,-25,8,11,-20,-19,-16,3,-22,-14,-30,-26,-6,-21,-29,-16,-29,5,-11,-26,-17,5,-28,16,-30,-18,13,15,-30,-8,27,-5,27,-9,28,25,8,-19,-12,28,14,-3,-15,-14,-23,-27,24,26,-15,11,-4,28,-14,-4,4,12,-2,18,23,29,-23,-24,-12,-26,19,0,-20,4,0,0,-16,0,13,18,-8,-5,-23,-13,-18,16,-29,12,13,21,22,-27,6,-14,-23,-15,20,26,2,-26,-16,-4,21,-3,-24,16,-26,-21,25,-8,15,1,12,-10,-28,-6,10,-29,-2,27,-12,-24,-25,-18,-14,13,20,16,-20,0,5,2,-5,-23,-15,-9,-13,12,-17,-11,-27,-21,20,1,5,-21,24,12,-30,14,-15,12,4,-29,-3,9,20,-19,-27,-22,-18,17,-27,-16,21,28,24,26,9,18,26,29,-6,-18,21,-25,18,-14,11,19,11,-3,4,29,-10,8,3,-15,24,3,10,9,7,-5,-12,16,-2,21,-3,29,23,12,-15,-15,-14,-13,-15,18,-13,-9,29,-10,-11,-11,-21,12,22,13,-9,10,26,-26,-6,14,-17,-12,-16,-25,-21,-28,-16,-27,29,12,-30,-24,-25,21,4,3,21,25,-16,5,0,-19,-17,10,-2,-28,15,-28,-30,27,-2,20,-16,-11,-2,11,2,-10,-3,17,18,-8,-18,-29,-24,-2,-13,-10,16,10,14,-12,0,-22,3,22,-19,-30,-8,-21,16,28,-16,-3,25,26,-27,-18,4,19,13,-10,-13,5,-7,-28,12,14,-19,-25,-13,12,-24,-12,-14,19,0,-27,21,7,25,24,16,-28,-1,10,0,23,7,-13,17,-14,-21,-20,-25,-21,-30,-7,-11,1,6,-19,27,21,-10,-21,4,9,-28,19,-30,27,-20,-30,-26,-11,-1,6,-23,12,-2,-22,14,19,-29,-17,-1,-18,-26,5,-10,0,19,13,15,-25,-4,7,-17,-21,-15,-21,13,-30,-25,-24,-17,3,-7,-2,5,-15,-9,-25,29,-25,2,-26,14,-26,18,-29,-14,23,-18,-6,12,-25,29,2,8,9,10,18,-6,16,19,16,-7,22,-12,-6,16,21,-2,27,19,1,-17,-18,21,23,23,-27,-21,-28,17,-19,-27,21,-2,-30,9,-16,-12,28,-20,5,8,-15,-23,19,-8,6,-27,-18,-5,-4,9,9,-26,18,-21,-16,-16,-5,12,-26,-20,2,27,-27,-13,-5,-21,3,-7,-24,7,8,5,4,-1,18,-11,29,-12,-26,29,4,29,28,-1,-1,1,-13,-8,11,17,2,1,-16,17,11,-28,23,-29,23,27,19,-28,-9,-4,11,-12,-26,-16,-21,-25,3,-7,2,-27,9,7,-11,18,-18,18,11,-11,-10,26,28,28,15,-19,27,-1,-21,-30,-28,-5,-8,19,8,22,-21,-16,18,-13,-17,23,-18,-17,-11,1,-21,11,-17,-1,21,-18,-14,26,-6,-4,21,-27,8,9,-1,-12,-15,23,-23,-5,10,-21,5,-3,-28,10,-17,7,16,9,27,21,27,0,-4,-25,-13,27,-15,6,-30,0,-27,21,1,3,20,23,-4,21,-20,-9,-12,-27,1,-28,-22,-20,11,0,28,-7,16,-5,-2,28,-6,13,-4,-16,-9,4,-25,24,10,1,-30,11,5,18,5,28,2,21,1,21,-21,-8,-13,20,-13,16,23,29,-5,12,-9,23,-11,7,-8,29,8,18,-7,25,-30,-11,7,-12,7,-10,17,-15,15,-29,22,-24,2,-3,-16,19,15,-3,-5,12,4]
print(solution.countRangeSum(nums,-17,-10))
