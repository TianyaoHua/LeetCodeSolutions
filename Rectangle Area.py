class Solution(object):
    def comp(self, A, B, C, D, E, F, G, H):
        height1 = D-B
        height2 = H-F
        if E >= C:
            return height1 * (C - A) + height2 * (G - E)
        else:
            if H <= B or F >= D:
                return height1 * (C - A) + height2 * (G - E)
            else:
                if G >= C:
                    if F <= B < H <= D:
                        return height1 * (C - A) + height2 * (G - E) - (H - B) * (C - E)
                    elif B <= F < D <= H:
                        return height1 * (C - A) + height2 * (G - E) - (D - F) * (C - E)
                    elif F <= B <= D <= H:
                        return height1 * (C - A) + height2 * (G - E) - height1 * (C - E)
                    elif B <= F <= H <= D:
                        return height1 * (C - A) + height2 * (G - E) - height2 * (C - E)
                else:
                    if F <= B < H <= D:
                        return height1 * (C - A) + height2 * (G - E) - (H - B) * (G - E)
                    elif B <= F < D <= H:
                        return height1 * (C - A) + height2 * (G - E) - (D - F) * (G - E)
                    elif F <= B <= D <= H:
                        return height1 * (C - A) + height2 * (G - E) - height1 * (G - E)
                    elif B <= F <= H <= D:
                        return height1 * (C - A) + height2 * (G - E) - height2 * (G - E)
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        if A <= E:
            return self.comp(A, B, C, D, E, F, G, H)
        else:
            temp = A
            A = E
            E = temp
            temp = B
            B = F
            F = temp
            temp = C
            C = G
            G = temp
            temp = D
            D = H
            H = temp
            return self.comp(A, B, C, D, E, F, G, H)

solution = Solution()
print(solution.computeArea(-2,-2,2,2,1,-3,3,3))