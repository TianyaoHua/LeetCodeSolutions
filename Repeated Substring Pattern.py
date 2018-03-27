class Solution(object):
    def gca(self,a,b):
        if a < b:
            a, b = b, a
        while b != 0:
            a, b = b, a % b
        return a
    def dis(self, a):
        q = []
        i = 2
        while i <= a:
            if a%i == 0:
                q.append(i)
                while a%i==0:
                    a = a // i
            i += 1
        return q
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        ls = len(s)
        if ls <= 1:
            return False
        dict = {}
        for c in s:
            if c not in dict:
                dict.update({c:0})
            dict[c] += 1
        statistic = [dict[c] for c in dict]
        if len(statistic) == 1:
            return True
        max_q = self.gca(statistic[0], statistic[1])
        qs = self.dis(max_q)
        n_q = len(qs)
        min_q_flag = False
        i = 0
        while i < n_q and not min_q_flag:
            min_q_flag = True
            for n in statistic[2:]:
                if n % qs[i] != 0:
                    min_q_flag = False
            i += 1
        if not min_q_flag:
            return False
        min_q = qs[i-1]
        unit = ls//min_q
        for i in range(min_q-1):
            if s[i*unit:(i+1)*unit] != s[(i+1)*unit:(i+2)*unit]:
                return False
        return True


print(Solution().repeatedSubstringPattern('aaaaaaaaaaaaaaaaaab'))
