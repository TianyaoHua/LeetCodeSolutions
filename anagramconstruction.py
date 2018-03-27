def solution(A, B):
    # write your code in Python 3.6
    dictA = {}
    dictB = {}
    for c in A:
        if c not in dictA:
            dictA[c] = 0
        dictA[c] += 1
    for c in B:
        if c not in dictB:
            dictB[c] = 0
        dictB[c] += 1
    answer = 0
    for c in dictA:
        if c not in dictB:
            answer += dictA[c]
        else:
            if dictA[c] != dictB[c]:
                answer += abs(dictA[c]-dictB[c])
            dictB[c] = 0
    for c in dictB:
        answer += dictB[c]
    return answer

print(solution('apple','pear'))