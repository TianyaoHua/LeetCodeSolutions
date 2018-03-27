class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums = list(i*3-target for i in nums)
        collection = {}
        for i in nums:
            if i not in collection:
                collection[i] = 0
            collection[i] += 1
        nums = sorted(nums)
        positive_num = list(num for num in nums if num > 0)
        pn_l = len(positive_num)
        non_positive_num = list(num for num in nums if num <=0)
        npn_l = len(non_positive_num)
        unique = sorted(collection.keys())
        positive = list(num for num in unique if num > 0)       #small to big
        non_positive = list(num for num in unique if num <= 0)  #small to big
        n_l = len(non_positive)
        p_l = len(positive)

        if (pn_l > 2 and npn_l > 2):
            answer = min(sum(positive_num[0:3]),sum(non_positive_num[-3:]))
            #answer = closest_dist
        if (pn_l > 2 and npn_l < 3):
            answer = sum(positive_num[0:3])
            #closest_dist = answer
        if (pn_l < 3 and npn_l > 2):
            answer = sum(non_positive_num[-3:])
            #closest_dist = - answer
        if (pn_l < 3 and npn_l < 3 and npn_l + npn_l > 2):
            answer = sum(nums[0:3])
            #closest_dist = abs(answer)
        if (pn_l + npn_l < 4):
            return sum(nums)/3 + target
        if (pn_l == 0 and npn_l > 2):
            return sum(nums[-3:])/3 + target
        if pn_l == 0 and npn_l < 3 :
            return sum(nums)/3 + target
        if npn_l == 0 and pn_l > 2:
            return sum(nums[0:3])/3 + target
        if npn_l == 0 and pn_l < 3:
            return sum(nums)/3 + target
        for i in range(0, n_l):
            pp = 0
            if collection.get(non_positive_num[i]) > 1:
                j_beginning = i
            else:
                j_beginning = i+1
            for j in range(j_beginning, n_l):
                inverse = -non_positive[i]-non_positive[j]
                while pp < p_l-1 and positive[pp] < inverse:
                    pp += 1
                answer1 = non_positive[i]+non_positive[j]+positive[pp]
                answer2 = non_positive[i]+non_positive[j]+positive[pp-1]
                answer = min([answer, answer1, answer2],key= lambda x:abs(x))
        for i in range(0, p_l):
            np = 0
            if collection.get(positive[i]) > 1:
                j_beginning = i
            else:
                j_beginning = i+1
            for j in range(j_beginning, p_l):
                inverse = -positive[i] - positive[j]
                while np < n_l-1 and non_positive[np] < inverse:
                    np += 1
                answer1 = positive[i] + positive[j] + non_positive[np]
                answer2 = positive[i] + positive[j] + non_positive[np-1]
                answer = min([answer, answer1, answer2],key=lambda x:abs(x))
        return answer/3 + target




if __name__ == "__main__":
    solution = Solution()
    answer = solution.threeSumClosest([1,1,1,1],0)
    print(answer)
