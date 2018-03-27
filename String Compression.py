class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        i = 0
        j = 0
        n = len(chars)
        while j < n:
            if chars[j] == chars[i]:
                j += 1
            elif j-i > 1:
                num = list(str(j-i))
                chars[i:j] = [chars[i]]+ num
                n = len(chars)
                j += (i-j+len(num)+1)
                i = j
            else:
                i = j
                j += 1
        if j - i > 1:
            num = list(str(j - i))
            chars[i:j] = [chars[i]] + num
        print(chars)
        return len(chars)

print(Solution().compress(["a","b","b","c","c","c",'d']))