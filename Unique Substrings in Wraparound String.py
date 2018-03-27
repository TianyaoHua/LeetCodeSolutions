class Solution(object):
    def check(self, string, pool):
        if string in pool:
            return 0
        elif string[1] == 1:
            pool.add(string)
            return 1
        else:
            answer = 0
            for i in range(string[0], string[0]+string[1]//2):
                j = (string[0]+string[1] - 1)
                while j >= (string[0]+string[1]//2) and (i%26, j-i+1) not in pool:
                    answer += 1
                    pool.add((i%26, j-i+1))
                    j -= 1
            answer += self.check((string[0], string[1]//2),pool)
            answer += self.check(((string[0]+string[1]//2)%26, string[1]-string[1]//2),pool)
            return answer

    def findSubstringInWraproundString(self, p):
        """
        :type p: str
        :rtype: int
        """
        dict = {i:ord(i)-97 for i in 'abcdefghijklmnopqrstuvwxyz'}
        n = len(p)
        i = 0
        j = 1
        a = []
        pool = set()
        while j < n:
            if dict[p[j]]-dict[p[j-1]] != 1 and not (dict[p[j]]==0 and dict[p[j-1]] == 25):
                a.append((dict[p[i]], j-i))
                i = j
            j += 1
        a.append((dict[p[i]], j-i))
        answer = 0
        for string in a:
            answer += self.check(string, pool)
        return answer

print(Solution().findSubstringInWraproundString('a'))
