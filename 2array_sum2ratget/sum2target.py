def find_elements(A, B, target):
    n = len(A)
    i = 0
    j = n-1
    while i<n and j > -1:
        if A[i] + B[j] > target:
            j = j-1
        elif A[i] + B[j] < target:
            i = i+1
        else:
            return [i,j]
    return []



if __name__ =="__main__":
    A = [1,3,3,4,5,6,78]
    B = [-4,4,7,9,13,14,80]
    target = 82
    answer = find_elements(A,B,target)
    print (answer)