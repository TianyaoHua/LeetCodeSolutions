class Solution(object):
    def heapify(self, A, i):
        left = 2*i+1
        right = 2*i+2
        if left < len(A) and A[left][0] < A[i][0]:
            smallest = left
        else:
            smallest = i
        if right < len(A) and A[right][0] < A[smallest][0]:
            smallest = right
        if smallest != i:
            temp = A[i][:]
            A[i] = A[smallest][:]
            A[smallest] = temp[:]
            self.heapify(A, smallest)

    def extract(self, A):
        if not A:
            return None
        minimum = A[0]
        A[0] = A[-1][:]
        A.pop()
        self.heapify(A,0)
        return minimum


    def insert(self, A, key):
        A.append(key)
        i = len(A)-1
        while i > 0 and A[(i-1)//2][0] > A[i][0]:
            temp = A[i][:]
            A[i] = A[(i-1)//2][:]
            A[(i-1)//2] = temp[:]
            i = (i-1)//2

    def next(self, i, j, nums1, nums2):
        i += 1
        j += 1
        while i < len(nums1)-1 and j < len(nums2)-1 and not(nums1[i] + nums2[j] <= nums1[i+1]+nums2[0] and nums1[i] + nums2[j] <= nums2[j+1]+nums1[0]):
            i += 1
            j += 1
        if i == len(nums1)-1:
            while j < len(nums2)-1 and not (nums1[i] + nums2[j] <= nums2[j + 1] + nums1[0]):
                j += 1
        elif j == len(nums2)-1:
            while i < len(nums1)-1 and not (nums1[i] + nums2[j] <= nums1[i + 1] + nums2[0]):
                i += 1
        return min(i, len(nums1)-1), min(j, len(nums2)-1)


    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        i = 0
        j = 0
        n1 = len(nums1)
        n2 = len(nums2)
        while (i+1)*(j+1)<k and (i < n1-1 or j < n2-1):
            i, j = self.next(i, j, nums1, nums2)
        answer = [[a,b] for a in nums1[0:i+1] for b in nums2[0:j+1]]
        answer.sort(key=lambda x:x[0]+x[1])
        return answer[0:k]


solution = Solution()
nums1=[1]
nums2=[3,5,6,7,8,100]

k = 10
print(solution.kSmallestPairs(nums1,nums2,k))