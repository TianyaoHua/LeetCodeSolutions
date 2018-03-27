class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        answer = ''
        if num == 0:
            return '0'
        elif num < 0:
            num = 2**32 + num
        dict = {0:'0',1:'1',2:'2',3:'3',4:'4',5:'5',6:'6',7:'7',8:'8',9:'9',10:'a',11:'b',12:'c',13:'d',14:'e',15:'f'}
        num = bin(num)[2:]
        n = len(num)
        r = n%4
        if r > 0:
            answer += dict[int(num[0:r],2)]
        for i in range(r,n-1,4):
            answer += dict[int(num[i:i+4],2)]
        return answer


solution = Solution()
print(solution.toHex(-5))
