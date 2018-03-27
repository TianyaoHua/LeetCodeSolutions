answer = 10
def A(n,k):
    s = 1
    for i in range(n, n-k, -1):
        s *= i
    return s
aaa = []
for n in range(2, 11):
    answer += 9*A(9,n-1)
    aaa.append(answer)
    print(answer)
print(aaa)