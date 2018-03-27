class Solution(object):
    def validIPAddress(self, IP):
        """
        :type IP: str
        :rtype: str
        """
        if '.' in IP and ':' not in IP:
            ip = IP.split('.')
            n = len(ip)
            if n != 4:
                return 'Neither'
            for i in range(4):
                s = ip[i]
                if not s.isdecimal():
                    return 'Neither'
                ns = int(s)
                if ns == 0 and len(s) > 1:
                    return 'Neither'
                if 0 < ns <= 255 and s[0] == '0':
                    return 'Neither'
                if ns < 0 or ns > 255:
                    return 'Neither'
            return 'IPv4'
        if ':' in IP and '.' not in IP:
            ip = IP.split(':')
            n = len(ip)
            if n != 8:
                return 'Neither'
            for i in range(8):
                s = ip[i]
                for c in s:
                    if not (48 <= ord(c) <= 57 or 97 <= ord(c) <= 102 or 65 <= ord(c) <= 70):
                        return 'Neither'
                ns = int(s,16)
                if ns<0 or ns>65535 or len(s) > 4:
                    return 'Neither'
            return 'IPv6'
        return 'Neither'

print(Solution().validIPAddress("2001:0db8:85a3:0:0:8A2E:0370:7334"))