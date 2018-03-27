class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(nums)
        if not n:
            return [-1,-1]
        l = 0
        r = n - 1
        p = int((r+l)/2)
        answer = []
        while r-p > 1 and p - l > 0:
            if nums[p] == target:
                a, b, c = l, p, r
                break
            elif nums[p] > target:
                r = p
                p = int((p+l)/2)
            else:
                l = p
                p = int((p+r)/2)
        if nums[p] == target:
            a, b, c = l, p, r
        elif nums[l] == target:
            a, b, c = l, l, r
        elif nums[r] == target:
            a, b, c = l, r, r
        else:
            return [-1,-1]
        l = a
        r = b
        p = int((a+b)/2)

        if nums[l] == target:
            answer.append(l)
        else:
            while r-p > 1 and p - l > 0:
                if nums[p] < target and nums[p+1] == target:
                    answer.append(p+1)
                    break
                elif nums[p] == target:
                    r = p
                    p = int((p+l)/2)
                else:
                    l = p
                    p = int((p+r)/2)
            if r-p == 1 and p != l:
                if nums[p] < target and nums[p+1] == target:
                    answer.append(p+1)
                if nums[r] < target and nums[r+1] == target:
                    answer.append(r+1)
                if nums[l] < target and nums[l+1] == target:
                    answer.append(l+1)
            if p == l and r-p != 1:
                if nums[p] < target and nums[p+1] == target:
                    answer.append(p+1)
                if nums[r] < target and nums[r+1] == target:
                    answer.append(r+1)
            if r-p == 1 and p == l:
                if nums[p] < target and nums[p+1] == target:
                    answer.append(p+1)
                if nums[r] < target and nums[r+1] == target:
                    answer.append(r + 1)

        l = b
        r = c
        p = int((l+r)/2)
        if nums[r] == target:
            answer.append(r)
        else:
            while r-p > 1 and p - l > 0:
                if nums[p] > target and nums[p-1] == target:
                    answer.append(p-1)
                    break
                elif nums[p] == target:
                    l = p
                    p = int((p+r)/2)
                else:
                    r = p
                    p = int((p+l)/2)
            if r-p == 1 and p != l:
                if nums[p] > target and nums[p-1] == target:
                    answer.append(p-1)
                if nums[r] > target and nums[r-1] == target:
                    answer.append(r-1)
                if nums[l] > target and nums[l-1] == target:
                    answer.append(l-1)
            if p == l and r-p != 1:
                if nums[p] > target and nums[p-1] == target:
                    answer.append(p-1)
                if nums[r] > target and nums[r-1] == target:
                    answer.append(r-1)
            if r-p == 1 and p == l:
                if nums[p] > target and nums[p-1] == target:
                    answer.append(p-1)
                if nums[r] > target and nums[r-1] == target:
                    answer.append(r - 1)
        return answer
if __name__ == "__main__":
    solution = Solution()
    nums = [0,0,1,1,2,2,2,2,3,3,4,4,4,5,6,6,6,7,8,8]
    answer = solution.searchRange(nums,4)
    print(answer)