class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        length = len(nums)
        if length < 4:
            return []
        i = 0
        j = 1
        p = 2
        q = length-1
        answer = []
        nums = sorted(nums)

        scan_direction = 1
        while i < length-4:
            while j < length-3:
                while q-p > 1:
                    if nums[i] + nums[j] + nums[p] + nums[q] < target:
                        p += 1
                        scan_direction = 0        #1: right 0: left
                        while nums[p] == nums[p-1] and p < q-1:
                            p += 1
                    elif nums[i] + nums[j] + nums[p] + nums[q] > target:
                        q -= 1
                        scan_direction = 1
                        while nums[q] == nums[q+1] and q > p+1:
                            q -= 1
                    else:
                        answer.append([nums[i], nums[j], nums[p], nums[q]])
                        p += 1
                        scan_direction = 0
                        while nums[p] == nums[p-1] and p < q-1:
                            p += 1
                if nums[i] + nums[j] + nums[p] + nums[q] == target and ((nums[p] != nums[p-1]) or scan_direction):
                    answer.append([nums[i], nums[j], nums[p], nums[q]]) ###################
                j += 1
                scan_direction = 0
                while nums[j] == nums[j-1] and j < length-3:
                    j += 1
                q = length-1
                p = j+1
            if nums[i] + nums[j] + nums[p] + nums[q] == target and (nums[j] != nums[j-1] or scan_direction):
                answer.append([nums[i], nums[j], nums[p], nums[q]])    ##################
            i += 1
            scan_direction = 0
            while nums[i] == nums[i-1] and i < length-4:
                i += 1
            j = i+1
            p = j+1
            q = length-1
        if nums[i] + nums[j] + nums[p] + nums[q] == target and (nums[i] != nums[i-1] or scan_direction):
            answer.append([nums[i], nums[j], nums[p], nums[q]])          ##############
        return answer


if __name__ == "__main__":
    solution = Solution()
    Answer = solution.fourSum([0,0,0,0],0)
    print(Answer)