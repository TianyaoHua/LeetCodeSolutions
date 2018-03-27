class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x<0:
            return False
        elif x > 999 or x < 10:
            e = -1
            temp = x
            while temp > 0:
                temp = (temp - (temp%10))/10
                e += 1
            if e%2 == 1:
                e = int((e+1)/2)
                lower = x%(10**e)
                higher = (x - lower)/10**e
                factor = 1
                for i in range(e-1):
                    factor = factor*10+1
            if e%2 == 0:
                e = int(e/2)
                lower = x%(10**e)
                higher = ((x - lower) / 10 ** e)
                higher = (higher-higher%10)/10
                factor = 1
                for i in range(e-1):
                    factor = factor*10+1
        elif x>=10 and x < 100:
            return x%10 == (x-x%10)/10
        else:
            return x%10 == (x-x%100)/100
        return not (higher+lower)%factor

if __name__=="__main__":
    solute = Solution()
    answer = solute.isPalindrome(121)
    print(answer)

#Bug! e.g:1122