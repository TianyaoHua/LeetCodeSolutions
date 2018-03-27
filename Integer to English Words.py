class Solution(object):
    def one_phase(self, s, dict):
        n = len(s)
        word = ''
        if n == 3:
            if s[0] != '0':
                word += dict[s[0]] + ' ' + 'Hundred' + ' '
                s = s[1:]
                n = 2
            else:
                s = s[1:]
                n = 2
        if n == 1:
            word += dict[s[0]]
        if n == 2:
            if s in dict:
                word += dict[s]
            else:
                if s[0] != '0':
                    word += dict[s[0]+'0'] + ' ' + dict[s[1]]
                elif s[1] != '0':
                    word += dict[s[1]]
        while word and word[-1] == ' ':
            word = word[0:-1]
        return word

    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        dict = {'1':'One', '2':'Two', '3':'Three', '4':'Four', '5':'Five', '6':'Six', '7':'Seven', '8':'Eight', '9':'Nine', '10':'Ten',
                '11':'Eleven', '12':'Twelve', '13':'Thirteen', '14':'Fourteen', '15':'Fifteen', '16':'Sixteen', '17':'Seventeen', '18':'Eighteen', '19':'Nineteen',
                '20':'Twenty', '30':'Thirty', '40':'Forty', '50':'Fifty', '60':'Sixty', '70':'Seventy', '80':'Eighty', '90':'Ninety'}
        dict2 = {0:'', 1: 'Thousand', 2:'Million', 3:'Billion'}
        s = str(num)
        l = len(s)
        n = l//3 + int(l%3 != 0)
        word = ''
        for i in range(n-1):
            segment = self.one_phase(s[l-(n-1-i)*3: l-(n-1-i)*3+3], dict)
            if segment:
                word += segment + ' ' + dict2[n-2-i]+' '
        segment = self.one_phase(s[0:l-3*n+3], dict)
        word = segment + ' ' + dict2[n-1] + ' '+word
        while word[-1] == ' ':
            word = word[0:-1]
        return word

solution = Solution()
print(solution.numberToWords(1000000))
# Two Billion One Hundred Forty Seven Million Four Hundred Eighty Three Thousand Six Hundred Forty Seven
# Two Billion One Hundred Forty Seven Million Four Hundred Eighty Three Thousand Six Hundred Forty Seven