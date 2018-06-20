# class Solution(object):
#     def f(self, boxes, i, j, i2, j2, h):
#         if (i, j, i2, j2) in h:
#             return h[(i, j, i2, j2)]
#         elif i == j and i2 == j2:
#             return 0
#         else:
#             index = {}
#             answer = 0
#             for p in range(i, j):
#                 if boxes[p] not in index:
#                     index[boxes[p]] = []
#                 index[boxes[p]].append(p)
#             for p in range(i2, j2):
#                 if boxes[p] not in index:
#                     index[boxes[p]] = []
#                 index[boxes[p]].append(p)
#             for key in index:
#                 number_key = len(index[key])
#                 score = number_key**2
#                 start_p = index[key][0]
#                 last_p = index[key][-1]
#                 for p in range(number_key-1):
#                     if index[key][p] < j and index[key][p+1] > i2:
#                         score += self.f(boxes, index[key][p]+1, j, index[key][p+1]+1, j2, h)
#                     else:
#                         score += self.f(boxes, index[key][p]+1, index[key][p+1], index[key][p+1], index[key][p+1], h)
#                 if i <= start_p < j and i2 <= last_p < j2:
#                     score += self.f(boxes, i, start_p, last_p + 1, j2, h)
#                 elif i <= start_p <= last_p < j:
#                     score += self.f(boxes, i, start_p, start_p, start_p, h)
#                     score += self.f(boxes, last_p+1, j, i2, j2, h)
#                 else:
#                     score += self.f(boxes, i2, start_p, start_p, start_p, h)
#                     score += self.f(boxes, last_p + 1, j2, j2, j2, h)
#                 if answer < score:
#                     answer = score
#             h[(i, j, i2, j2)] = answer
#             return answer
#
#     def removeBoxes(self, boxes):
#         """
#         :type boxes: List[int]
#         :rtype: int
#         """
#         h = {}
#         # index = {}
#         # answer = 0
#         # for p in range(len(boxes)):
#         #     if boxes[p] not in index:
#         #         index[boxes[p]] = []
#         #     index[boxes[p]].append(p)
#         # for key in index:
#         #     if len(index[key]) == 1:
#         #         answer += 1
#         #         boxes[index[key][0]] = 'e'
#         # boxes = list(filter(lambda x: x != 'e', boxes))
#         return self.f(boxes, 0, len(boxes), len(boxes), len(boxes), h)


#print(Solution().removeBoxes([86,26,80,27,1,16,78,71,36,52,65,76,58,77,45,17,100,37,37,75,49,2,37,42,19,99,14,33,34,58,4,30,100,88,74,47,80,77,85,32,80,35,80,25,60,91,99,27,47,66,13,20,15,10,26,39,60,9,63,24,66,32,29,79,67,19,88,35,44,67,22,99,27,27,40,78,2,21,40,69,88,26,57,23,15,70,1,100,37,20,26,18,27,86,88,33,28,40,92,15]))
#print(Solution().removeBoxes(range(100)))
