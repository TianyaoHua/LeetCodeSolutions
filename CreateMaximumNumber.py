class Solution(object):
    def merge(self, num1, num2,n,m,dict):
        table = [['' for j in range(m+1)] for i in range(n+1)]
        int_table = [[0 for j in range(m+1)] for i in range(n+1)]
        base_table = [[1 for j in range(m+1)] for i in range(n+1)]
        for i in range(n-1,-1,-1):
            table[i][m] = (num1[i:])
            int_table[i][m] = int_table[i+1][m] + dict[num1[i]]*base_table[i+1][m]*10
            base_table[i][m] = base_table[i+1][m]*10
        for j in range(m-1,-1,-1):
            table[n][j] = (num2[j:])
            int_table[n][j] = int_table[n][j+1] + dict[num2[j]]*base_table[n][j+1]*10
            base_table[n][j] = base_table[n][j+1]*10
        for i in range(n-1, -1, -1):
            for j in range(m-1,-1,-1):
                a = num1[i] + table[i+1][j]
                b = num2[j] + table[i][j+1]
                int_a = dict[num1[i]]*base_table[i+1][j]*10 + int_table[i+1][j]
                int_b = dict[num2[j]]*base_table[i][j+1]*10 + int_table[i][j+1]
                base_table[i][j] = base_table[i+1][j]*10
                table[i][j] = (int_a>=int_b)*a+(int_a<int_b)*b
        return table[0][0]

    def maxNumber(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[int]
        """
        dict = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
        int_nums1 = nums1[:]
        int_nums2 = nums2[:]
        nums1 = [str(i) for i in nums1]
        nums2 = [str(i) for i in nums2]
        n = len(nums1)
        m = len(nums2)
        table1 = [['' for i in range(n+1)] for j in range(k+1)]
        int_table1 = [[0 for i in range(n+1)] for j in range(k+1)]
        base_table1 = [[1 for i in range(n+1)] for j in range(k+1)]
        table2 = [['' for i in range(m+1)] for j in range(k+1)]
        int_table2 = [[0 for i in range(m+1)] for j in range(k+1)]
        base_table2 = [[1 for i in range(m+1)] for j in range(k+1)]
        for p in range(1, k+1):
            for i in range(n - p, -1, -1):
                a = nums1[i] + table1[p-1][i+1]
                b = table1[p][i+1]
                int_a = int_nums1[i]*base_table1[p-1][i+1]*10+int_table1[p-1][i+1]
                int_b = int_table1[p][i+1]
                table1[p][i] = a*(int_a >= int_b) + b*(int_a < int_b)
                int_table1[p][i] = int_a*(int_a > int_b) + int_b*(int_a <= int_b)
                base_table1[p][i] = base_table1[p-1][i]*10
        for p in range(1, k+1):
            for j in range(m-p,-1,-1):
                a = nums2[j] + table2[p-1][j+1]
                b = table2[p][j+1]
                int_a = int_nums2[j]*base_table2[p-1][j+1]*10+int_table2[p-1][j+1]
                int_b = int_table2[p][j+1]
                table2[p][j] = a*(int_a >= int_b) + b*(int_a < int_b)
                int_table2[p][j] = int_a*(int_a >= int_b) + int_b*(int_a < int_b)
                base_table2[p][j] = base_table2[p-1][j]*10
        answer = '0'
        int_answer = 0
        for i in range(max(k-m, 0), min(n, k)+1):
            candidate = self.merge(table1[i][0], table2[k-i][0], i, k-i,dict)
            int_candidate = int(candidate)
            if int_answer < int_candidate:
                answer = candidate
                int_answer = int_candidate
        return answer

def f():
    a = [1,3,4]
    b = [2,4,6]
    c = [max(a,b).pop(0) for _ in a+b]
solution = Solution()
nums1=[4,6,9,1,0,6,3,1,5,2,8,3,8,8,4,7,2,0,7,1,9,9,0,1,5,9,3,9,3,9,7,3,0,8,1,0,9,1,6,8,8,4,4,5,7,5,2,8,2,7,7,7,4,8,5,0,9,6,9,2]
nums2=[9,9,4,5,1,2,0,9,3,4,6,3,0,9,2,8,8,2,4,8,6,5,4,4,2,9,5,0,7,3,7,5,9,6,6,8,8,0,2,4,2,2,1,6,6,5,3,6,2,9,6,4,5,9,7,8,0,7,2,3]
k=60
nums1=[3,4,6,5]
nums2=[9,1,2,5,8,3]
k=6
#print(solution.merge('1',''))
print(solution.maxNumber(nums1,nums2,k))