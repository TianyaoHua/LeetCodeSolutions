class Solution(object):
    def method(self, coins, n, amount, dict):
        if amount == 0 and n >=0:
            return 0
        elif amount < 0 or n < 0:
            return float('inf')
        else:
            if n in dict and amount in dict[n]:
                return dict[n][amount]
            else:
                n_coins = min(1+self.method(coins, n, amount-coins[n],dict), self.method(coins, n-1, amount, dict))
                if n not in dict:
                    dict.update({n:{}})
                dict[n].update({amount:n_coins})
                return n_coins
    def DFS(self, coins, u, value,time,amount):
        time += 1
        value += u
        answer = 100000
        if value == amount:
            return time
        if value > amount:
            return 100000
        else:
            for v in coins:
                answer = self.DFS(coins, v, value, time, amount)
                if answer < 100000:
                    return answer
            return answer

    def coinChange(self, coins, amount):
        s = {0}
        i = 0
        while s and amount not in s:
            s = {v+c for v in s for c in coins if v+c <= amount}
            i += 1
        if s:
            print(s)
            return i
        return -1


solution = Solution()
coins = [181,79,206,169,487,319,262,162,420]
print(solution.coinChange(coins,4409))

