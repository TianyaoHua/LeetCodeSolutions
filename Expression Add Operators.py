class Solution(object):
    def isExist(self, num, target):
        n = len(num)
        if not n:
            return False
        a = [[set() for i in range(n)] for j in range(n)]
        for i in range(n):
            a[i][i].add(int(num[i]))
        for l in range(1, n):
            for i in range(n-l):
                j = i + l
                if num[i] != '0':
                    a[i][j].add(int(num[i:j+1]))
                for k in range(i, j):
                    for value1 in a[i][k]:
                        for value2 in a[k+1][j]:
                            a[i][j].add(value1*value2)
        for l in range(1, n):
            for i in range(n-l):
                j = i + l
                for k in range(i, j):
                    for key1 in a[i][k]:
                        for key2 in a[k+1][j]:
                            a[i][j].add(key1-key2)
                            a[i][j].add(key1+key2)
        return target in a[0][n-1]

    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        # flag = self.isExist(num, target)
        # if not flag:
        #     return []
        n = len(num)
        a = [[{} for i in range(n)] for j in range(n)]
        value = {}
        for i in range(n):
            int_num = int(num[i])
            a[i][i] = {int_num: {num[i]}}
            value.update({num[i]: int_num})
        for l in range(1, n):
            for i in range(n-l):
                j = i + l
                if num[i] != '0':
                    int_num = int(num[i:j+1])
                    a[i][j] = {int_num: {num[i:j+1]}}
                    value.update({num[i:j+1]: int_num})
                for k in range(i, j):
                    for key1 in a[i][k]:
                        for key2 in a[k+1][j]:
                            key = key1*key2
                            if key not in a[i][j]:
                                a[i][j].update({key: set()})
                            for string1 in a[i][k][key1]:
                                for string2 in a[k+1][j][key2]:
                                    a[i][j][key].add(string1 + '*' + string2)
                                    value.update({string1 + '*' + string2: key})
        for l in range(1, n-1):
            for i in range(n-l):
                j = i + l
                for k in range(i, j):
                    for key1 in a[i][k]:
                        for key2 in a[k+1][j]:
                            key = key1 + key2
                            if key not in a[i][j]:
                                a[i][j].update({key: set()})
                            for string1 in a[i][k][key1]:
                                for string2 in a[k+1][j][key2]:
                                    a[i][j][key].add(string1 + '+' + string2)
                                    value.update({string1 + '+' + string2: key})
                            for string1 in a[i][k][key1]:
                                for string2 in a[k+1][j][key2]:
                                    index_plus = string2.find('+')
                                    index_minus = string2.find('-')
                                    if index_plus == -1 and index_minus == -1:
                                        key2_s = key2
                                    elif index_plus == -1:
                                        key2_s = -key2 + 2 * value[string2[0: index_minus]]
                                    elif index_minus == -1:
                                        key2_s = -key2 + 2 * value[string2[0: index_plus]]
                                    else:
                                        key2_s = -key2 + 2 * value[string2[0: min(index_minus, index_plus)]]
                                    if key1 - key2_s not in a[i][j]:
                                        a[i][j].update({key1 - key2_s: set()})
                                    a[i][j][key1 - key2_s].add(string1 + '-' + string2)
                                    value.update({string1 + '-' + string2: key1 - key2_s})
        i = 0
        j = n-1
        for k in range(i, j):
            for key1 in a[i][k]:
                for key2 in a[k + 1][j]:
                    key = key1 + key2
                    if key == target:
                        if key not in a[i][j]:
                            a[i][j].update({key: set()})
                        for string1 in a[i][k][key1]:
                            for string2 in a[k + 1][j][key2]:
                                a[i][j][key].add(string1 + '+' + string2)
                                value.update({string1 + '+' + string2: key})
                    for string1 in a[i][k][key1]:
                        for string2 in a[k + 1][j][key2]:
                            index_plus = string2.find('+')
                            index_minus = string2.find('-')
                            if index_plus == -1 and index_minus == -1:
                                key2_s = key2
                            elif index_plus == -1:
                                key2_s = -key2 + 2 * value[string2[0: index_minus]]
                            elif index_minus == -1:
                                key2_s = -key2 + 2 * value[string2[0: index_plus]]
                            else:
                                key2_s = -key2 + 2 * value[string2[0: min(index_minus, index_plus)]]
                            if key1 - key2_s == target:
                                if key1 - key2_s not in a[i][j]:
                                    a[i][j].update({key1 - key2_s: set()})
                                a[i][j][key1 - key2_s].add(string1 + '-' + string2)
                                value.update({string1 + '-' + string2: key1 - key2_s})
        return a[0][n-1][target]


solution = Solution()
print(solution.addOperators('2358774456',2358774456))
