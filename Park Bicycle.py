def solution(A):
    # write your code in Python 3.6
    A.sort()
    n = len(A)
    distance = 0
    for i in range(n-1):
        distance = max(distance, (A[i+1]-A[i])//2)
    return distance

print(solution([-3,-1,4,2,0,9]))
