class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        set1 = {'q','w','e','r','t','y','u','i','o','p','Q','W','E','R','T','Y','U','I','O','P'}
        set2 = {'a','s','d','f','g','h','j','k','l','A','S','D','F','G','H','J','K','L'}
        set3 = {'z','x','c','v','b','n','m','Z','X','C','V','B','N','M'}
        answer = []
        for word in words:
            if len(word) == 0:
                answer.append(word)
            else:
                if word[0] in set1:
                    flag = 1
                    for c in word:
                        if c not in set1:
                            flag = 0
                            break
                    if flag:
                        answer.append(word)
                elif word[0] in set2:
                    flag = 1
                    for c in word:
                        if c not in set2:
                            flag=0
                            break
                    if flag:
                        answer.append(word)
                elif word[0] in set3:
                    flag = 1
                    for c in word:
                        if c not in set3:
                            flag = 0
                            break
                    if flag:
                        answer.append(word)
        return answer

words = ["Hello", "Alaska", "Dad", "Peace"]
print(Solution().findWords(words))
