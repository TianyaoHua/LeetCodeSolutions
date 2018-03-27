def solution(S):
    # write your code in Python 3.6
    n = len(S)
    table1 = [0]*(n+1)
    table2 = [0]*(n+1)
    for i in range(n):
        if S[i] == '(':
            table1[i+1] = table1[i]+1
        else:
            table1[i+1] = table1[i]
    for i in range(n-1,-1,-1):
        if S[i] == ')':
            table2[i] = table2[i+1]+1
        else:
            table2[i] = table2[i+1]
    for k in range(n+1):
        if table1[k] == table2[k]:
            return k
    return -1


print(solution(')'))