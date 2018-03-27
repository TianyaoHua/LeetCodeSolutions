class Solution(object):
    def line(self, words, n, maxWidth):
        length_of_words = sum(len(words[i]) for i in range(n))
        number_of_splits = n - 1
        number_of_spaces = maxWidth-length_of_words
        line = words[0]
        if number_of_splits == 0:
            line += ' '*number_of_spaces
        elif number_of_spaces % number_of_splits:
            l_smaller = (number_of_spaces//number_of_splits)
            smaller = ' ' * l_smaller
            l_bigger = (number_of_spaces//number_of_splits+1)
            bigger = ' '*l_bigger
            for i in range(1, n):
                if number_of_spaces % number_of_splits:
                    line += bigger
                    line += words[i]
                    number_of_spaces -= l_bigger
                    number_of_splits -= 1
                else:
                    line += smaller
                    line += words[i]
                    number_of_spaces -= l_smaller
                    number_of_splits -= 1
        else:
            spaces = ' '*(number_of_spaces//number_of_splits)
            for i in range(1, n):
                line += spaces
                line += words[i]
        return line

    def last_line(self, words, n, maxWidth):
        last_line = words[0]
        for i in range(1, n):
            last_line = last_line + ' '+words[i]
        last_line += ' '*(maxWidth-len(last_line))
        return last_line

    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        n = len(words)
        justified_text = []
        i = 0
        j = 0
        s_length = 0
        while i < n-1:
            s_length += len(words[i])
            if s_length + len(words[i+1]) + i - j + 1 > maxWidth:
                a_line = self.line(words[j:i+1], i+1-j, maxWidth)
                justified_text.append(a_line)
                j = i+1
                s_length = 0
            i += 1
        last_line = self.last_line(words[j:i+1], i+1-j, maxWidth)
        justified_text.append(last_line)
        return justified_text

if __name__ == "__main__":
    solution = Solution()
    words = ["a", "b", "c", "d"]
    text = solution.fullJustify(words, 1)
    print(text)