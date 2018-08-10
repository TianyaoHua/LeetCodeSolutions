class Solution:
    def smaller(self, special, needs):
        for i in range(len(needs)):
            if special[i] > needs[i]:
                return False
        return True
    def diff(self, needs, special):
        needs_ = [0]*len(needs)
        for i in range(len(needs)):
            needs_[i] = needs[i] - special[i]
        return tuple(needs_)
    def core(self, price, special, needs, records):
        if needs in records:
            return records[needs]
        else:
            answer = float("infinity")
            for special_ in special:
                if self.smaller(special_, needs):
                    needs_ = self.diff(needs, special_)
                    answer = min(answer, special_[-1] + self.core(price, special, needs_, records))
            no_special = 0
            for j in range(len(needs)):
                no_special += needs[j]*price[j]
            answer = min(answer, no_special)
            records[needs] = answer
            return answer

    def shoppingOffers(self, price, special, needs):
        """
        :type price: List[int]
        :type special: List[List[int]]
        :type needs: List[int]
        :rtype: int
        """
        needs = tuple(needs)
        return self.core(price, special, needs, {})


print(Solution().shoppingOffers([2,3,4], [[1,1,0,4],[2,2,1,9]], [1,2,1]))