class Solution(object):
    def analyse(self, s, n):
        layer = 0
        file = False
        for  i in range(1, n):
            if s[i] == '\t':
                layer += 1
            if s[i] == '.':
                file = True
        return layer,file

    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """
        i = 0
        j = 1
        input = '\n'+input
        dict = {}
        answer = 0
        while j < len(input):
            while j < len(input) and input[j] != '\n':
                j += 1
            layer, file =self.analyse(input[i:j], j-i)
            if layer not in dict:
                dict.update({layer: []})
            if layer > 0:
                length = j-i-layer-1 + dict[layer-1][-1]+1
                dict[layer].append(length)

            else:
                length = j-i-layer-1
                dict[layer].append(length)
            if file:
                answer = max(answer, length)
            i = j
            j += 1
        return answer

solution = Solution()
print(solution.lengthLongestPath("dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext"))