class Solution(object):
    def check(self, subarray, dictionary, n_words, l_words):
        temp = dictionary.copy()
        for i in range(n_words):
            point = i * l_words
            temp_word = subarray[point:point+l_words]
            if  temp_word in temp:
                if temp.get(temp_word) > 0:
                    temp[temp_word] -= 1
                else:
                    return False
            else:
                return False
        return True

    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        n_words = len(words)
        l_words = len(words[0])
        n_s = len(s)
        unit = n_words * l_words
        dictionary = {}
        answer = []
        for word in words:
            if word not in dictionary:
                dictionary[word] = 0
            dictionary[word] += 1
        for i in range(n_s - unit + 1):
            if answer and (i - answer[-1]) == l_words:
                if s[i-l_words : i] == s[i+unit-l_words : i+unit]:
                    answer.append(i)
            elif s[i:i+l_words] in dictionary:
                if self.check(s[i: i+unit],dictionary,n_words,l_words):
                    answer.append(i)
        return answer

if __name__ =="__main__":
    solution = Solution()
    answer1 = solution.findSubstring("aaaaaaaaaa",['a','a','a','a'])
    print(answer1)











