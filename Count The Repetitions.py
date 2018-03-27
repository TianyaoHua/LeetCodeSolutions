class Solution(object):
    def getMaxRepetitions(self, s1, n1, s2, n2):
        """
        :type s1: str
        :type n1: int
        :type s2: str
        :type n2: int
        :rtype: int
        """
        set1, set2 = set(s1), set(s2)
        for c in set2:
            if c not in set1:
                return 0
        for c in set1:
            if c not in set2:
                s1 = s1.replace(c, '')
        table = {}
        index = 0
        l1, l2 = len(s1), len(s2)
        while index not in table:
            i, j, m = index, 0, 0
            while j < l2:
                if s1[i] == s2[j]:
                    i, j = i+1, j+1
                else:
                    i += 1
                m += 1
                if i >= l1:
                    i = 0
            table.update({index:[i,m]})
            index = i
        BigTable = {}
        M, l1_,p, index = 0, n1*l1, 0, 0
        shortpath = 0
        while p <= l1_:
            M += 1
            if index in BigTable:
                index = BigTable[index][0]
                p += BigTable[index][1]
            else:
                current_index = index
                current_p = p
                for j in range(n2):
                    p += table[index][1]
                    index = table[index][0]
                BigTable.update({current_index:[index, p-current_p]})
            if p%l1 == 0:
                shortpath = 1
                break
        if shortpath:
            return l1_//p*M
        return M-1




print(Solution().getMaxRepetitions('acb',4,'ab',2))