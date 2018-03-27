class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        path = path.split('/')

        simplified = []
        while '' in path:
            path.remove('')
        n = len(path)
        for i in range(n):
            k = len(path[i])
            if path[i] == '.'*k:
                simplified = simplified[0:max(0,len(simplified)-k)]
            else:
                simplified.append(path[i])
        simplified_path = ''
        for s in simplified:
            simplified_path += '/'+ s
        if not simplified_path:
            return '/'
        return simplified_path

if __name__ == "__main__":
    solution = Solution()
    path = "/"
    answer = solution.simplifyPath(path)
    print(answer)


