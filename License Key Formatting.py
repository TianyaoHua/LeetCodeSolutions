class Solution(object):
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        S = S.replace('-','')
        i = len(S)-K
        answer = ''
        while i > 0:
            answer = S[i:i+K]+'-'+answer
            i -= K
        answer = S[0:i+K] + '-' + answer
        return answer
print(Solution().licenseKeyFormatting("r",1))