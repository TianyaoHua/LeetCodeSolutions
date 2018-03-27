class Solution(object):
    def maxNumber(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[int]
        """
        nums1 = [str(i) for i in nums1]
        nums2 = [str(i) for i in nums2]
        n = len(nums1)
        m = len(nums2)
        table = [[['' for j in range(m+1)] for i in range(n+1)] for p in range(k+1)]
        i = n
        for p in range(1, k+1):
            for j in range(m-p,-1,-1):
                a = nums2[j] + table[p-1][i][j+1]
                b = table[p][i][j+1]
                if b:
                    if int(a) > int(b):
                        table[p][i][j] = a
                    else:
                        table[p][i][j] = b
                else:
                    table[p][i][j] = a
        j = m
        for p in range(1, k+1):
            for i in range(n-p, -1, -1):
                a = nums1[i] + table[p-1][i+1][j]
                b = table[p][i+1][j]
                if b:
                    if int(a) > int(b):
                        table[p][i][j] = a
                    else:
                        table[p][i][j] = b
                else:
                    table[p][i][j] = a

        for p in range(1, k+1):
            for i in range(min(n-1,n+m-p),-1, -1):
                for j in range(min(m-1,m+n-p-i), -1, -1):
                    a = nums1[i] + table[p-1][i+1][j]
                    int_a = int(a)
                    b = nums2[j] + table[p-1][i][j+1]
                    int_b = int(b)
                    c = table[p][i][j+1]
                    d = table[p][i+1][j]
                    if int_a > int_b:
                        s = a
                        int_s = int_a
                    else:
                        s = b
                        int_s = int_b
                    if c:
                        int_c = int(c)
                        if int_c > int_s:
                            s = c
                            int_s = int_c
                    if d and int(d) > int_s:
                            s = d
                    table[p][i][j] = s
        return table[k][0][0]

solution = Solution()
nums1=[4,6,9,1,0,6,3,1,5,2,8,3,8,8,4,7,2,0,7,1,9,9,0,1,5,9,3,9,3,9,7,3,0,8,1,0,9,1,6,8,8,4,4,5,7,5,2,8,2,7,7,7,4,8,5,0,9,6,9,2]
nums2=[9,9,4,5,1,2,0,9,3,4,6,3,0,9,2,8,8,2,4,8,6,5,4,4,2,9,5,0,7,3,7,5,9,6,6,8,8,0,2,4,2,2,1,6,6,5,3,6,2,9,6,4,5,9,7,8,0,7,2,3]
k=60
print(solution.maxNumber(nums1,nums2,k))
