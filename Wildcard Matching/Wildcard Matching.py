class Solution(object):
    def isequal(self, a, b):
        n_a = len(a)
        n_b = len(b)
        if n_a != n_b:
            return False
        else:
            for i in range(n_a):
                if a[i] != b[i] and a[i] != '?' and b[i] != '?':
                    return False
        return True

    def substring(self, s, sub, n_sub, n_s):   # n_sub and n_s can not be 0!
        state = 0
        i = 0
        start_position = -1
        if n_sub:
            while i < n_s:
                if s[i] == sub[state] or sub[state] == '?':
                    state += 1
                    if start_position < 0:
                        start_position = i
                elif state:
                    state = 0
                    i = start_position
                    start_position = -1
                if state == n_sub:
                    return start_position
                i += 1
            return -1
        else:
            return 0

    def isMatch_core(self, s, p, s_left, s_right, p_left, p_right):
        if p_left == p_right:
            return True
        else:
            i = p_left + 1
            while p[i] != '*':
                i += 1
            segment = p[p_left+1: i]
            segment_position = self.substring(s[s_left: s_right + 1], segment, i-p_left-1, s_right-s_left+1)
            if segment_position == -1:
                return False
            else:
                return self.isMatch_core(s, p, s_left+segment_position+i-p_left-1, s_right, i, p_right)

    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        n_p = len(p)
        n_s = len(s)
        i = 0
        while i < n_p and p[i] != '*':
            i += 1
        left = i
        if left == n_p:
            if self.isequal(s,p):            #################
                return True
            else:
                return False
        else:
            i = n_p-1
            while i > -1 and p[i] != '*':
                i -= 1
            right = i
            if left-right+n_p-1 <= n_s and self.isequal(s[0:left], p[0:left]) and self.isequal(s[n_s-n_p+right+1:], p[right+1:]):
                return self.isMatch_core(s,p,left,n_s-n_p+right,left,right)
            else:
                return False

if __name__ == "__main__":
    solution = Solution()
    s = "mississippi"
    p = "m*issip*"

    answer = solution.isMatch(s,p)
    print(answer)
