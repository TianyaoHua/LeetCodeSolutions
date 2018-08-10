class Solution(object):
    def exclusiveTime(self, n, logs):
        """
        :type n: int
        :type logs: List[str]
        :rtype: List[int]
        """
        answer = [0]*n
        q = []
        time = 0
        for log in logs:
            r = log.split(':')
            id_ = int(r[0])
            timestamp = int(r[-1])
            state = r[1]
            if state == 'start':
                if q:
                    answer[q[-1]] += timestamp - time
                time = timestamp
                q.append(id_)
            else:
                task = q.pop()
                answer[task] += timestamp - time + 1
                time = timestamp + 1
        return answer



n = 2
logs = ["0:start:0","1:start:2","1:end:2","1:start:4","1:end:4","0:end:6"]
print(Solution().exclusiveTime(n, logs))