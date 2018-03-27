# s="catsanddog"
# dict = ["cat", "cats", "and", "sand", "dog"]

class Solution:
    def wordbreakkernel(self, s, wordDict, dic):
        if s in dic:
            return dic[s]
        elif len(s) == 0:
            return ['']
        else:
            result = []
            for word in wordDict:
                if s.find(word) == 0:
                    after_results = self.wordbreakkernel(s[len(word):],wordDict, dic)
                    for r in after_results:
                        result.append(word+' '+r)
            dic[s] = result
            return result


    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        dic = {}
        return self.wordbreakkernel(s, wordDict, dic)


# Q = [0]
#     Q_answer = ['']
#     n = len(s)
#     i = 0
#     check_dict = {}
#     answer = []
#     while i < len(Q):
# #       v = Q.pop(0)
# #       a = Q_answer.pop(0)
#       v = Q[i]
#       a = Q_answer[i]
#       i += 1
#       if v == n:
#         answer.append(a[:-1])
#       for word in wordDict:
#         if (v, word) in check_dict:
#           index = check_dict[(v,word)]
#         else:
#           index = s[v:].find(word)
#           check_dict[(v,word)] = index
#         if index==0:
#           Q.append(v+len(word))
#           Q_answer.append(a+word+' ')
#     return answer
s = 'aaaaaaaaaaaaa'
dic = ["a", "aa", "aaa"]
print(Solution().wordBreak(s, dic))