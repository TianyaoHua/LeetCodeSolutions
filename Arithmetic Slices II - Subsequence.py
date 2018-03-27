# class Solution(object):
#     def check(self, A, a, i, diff, threshold, dict):
#         if (i, diff, threshold) in dict:
#             return dict[(i,diff, threshold)]
#         else:
#             answer = 0
#             next_value = A[i]+diff
#             has_next = 0
#             k = 0
#             if next_value in a:
#                 n_next_value = len(a[next_value])
#                 while k < n_next_value and a[next_value][k] <= i:
#                     k += 1
#                 has_next = k < n_next_value
#             if not has_next and threshold == 0:
#                 return 1
#             elif has_next:
#                 while k < n_next_value:
#                     if a[next_value][k] > i:
#                         answer += self.check(A,a,a[next_value][k],diff,max(0,threshold-1),dict)
#                     k += 1
#                 dict.update({(i,diff,threshold): answer})
#                 print((i,diff,threshold,answer))
#             return answer
#     def numberOfArithmeticSlices(self, A):
#         """
#         :type A: List[int]
#         :rtype: int
#         """
#         a = {}
#         n = len(A)
#         for i in range(n):
#             if A[i] not in a:
#                 a.update({A[i]:[]})
#             a[A[i]].append(i)
#         answer = 0
#         dict = {}
#         for i in range(n):
#             for j in range(i+1,n):
#                 diff = A[j]-A[i]
#                 answer += self.check(A,a,i,diff,2,dict)
#         return answer
class Solution(object):
    def DFS(self, A, a, i, diff, dict):
        if (i, diff) in dict:
            return dict[(i, diff)]
        answer = [0, 0, 1]
        neighbour = A[i] + diff
        if neighbour not in a:
            dict.update({(i, diff): answer})
            return answer
        else:
            for index in a[neighbour]:
                if index > i:
                    temp = self.DFS(A, a, index, diff, dict)
                    answer[0] += temp[0]+temp[1]
                    answer[1] += temp[2]
            dict.update({(i, diff): answer})
            return answer

    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        n = len(A)
        a = {}
        for i in range(n):
            if A[i] not in a:
                a.update({A[i]: []})
            a[A[i]].append(i)
        dict = {}
        answer = 0
        visited = set()
        for i in range(n):
            for j in range(i + 1, n):
                diff = A[j] - A[i]
                if (i, diff) not in visited:
                    visited.add((i, diff))
                    if (i, diff) in dict:
                        answer += dict[(i,diff)][0]
                    elif A[j] + diff in a:
                        answer += self.DFS(A, a, i, diff, dict)[0]
        return answer


A = [-3229,-8962,-7486,9926,8464,-5806,-4511,-6770,-9229,-2089,-10921,-3196,681,6561,-9023,6689,2358,7785,7806,-2888,6966,-2145,672,-3626,6645,5078,7044,5277,9308,699,6838,2953,-10616,-6521,6854,-1641,-622,-8678,2965,1769,9076,-3,-3091,6903,-7558,10700,10016,7955,-174,-5183,894,-7371,-9414,-1021,-243,-6782,8393,-1435,-10813,7170,-2783,5228,2171,-3569,-761,-6484,-671,9360,-8843,-4081,9014,9250,-2279,4218,-9265,-7517,7185,7606,-9368,10895,399,-79,-9352,-7980,-5039,5531,4919,-7600,10220,11080,1773,6495,-5521,7545,2496,-9245,2943,-9012,4170,-7729,-7757,2342,-4682,1400,9450,-4568,-4252,-4147,1947,5868,6384,-9704,8161,-3825,4411,10453,-8503,8621,836,-4358,-10169,6240,10302,-8984,2851,-3792,-943,7268,-7013,-6491,-5278,-699,8978,258,3266,-9625,675,-3600,6257,-5633,-9687,-3001,-3075,-3232,3510,-10677,8950,9023,-4858,10496,-2520,8629,-5730,7406,812,5317,-9346,9085,7922,-9023,8119,9481,-4916,10861,-6109,-8551,-4451,10348,4941,-8082,9749,-7019,2972,3843,-2476,-8678,6432,-8408,865,405,1129,980,6891,687,-2129,4546,-2434,5744,70,9129,-9468,11220,-493,4893,-8844,11118,-8610,-3939,7457,-10840]
print(Solution().numberOfArithmeticSlices(A))