def solution(A):
    # write your code in Python 3.6
    n = len(A)
    if n == 1:
        return 1
    i = 0
    ToBeVisited = set(A)
    ToBeVisited.remove(A[0])
    answer = n
    for j in range(1, n):
        if A[i] == A[j]:
            i += 1
            while i < j and A[i] == A[i+1]:
                i += 1
        else:
            if A[j] in ToBeVisited:
                ToBeVisited.remove(A[j])
        if not ToBeVisited:
            answer = min(answer, j-i+1)
    return answer

print(solution([1,1,2,1,4,7,1,8]))

