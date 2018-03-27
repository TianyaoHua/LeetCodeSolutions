def wfs(a,v,n):
    if n > 0:
        n_v = len(v)
        v = v*len(a)
        for i in range(len(v)):
            v[i] = v[i]+[(a[int(i/n_v)])]
        return wfs(a, v, n-1)
    else:
        #answer = v[:]
        return v

def dfs(a,v,n,answer):
    if n > 0:
        for element in a:
            temp = v[:]
            v.append(element)
            dfs(a,v,n-1,answer)
            v = temp[:]
    else:
        answer.append(v)


if __name__ == "__main__":
    array = [1,2,3,4]
    v =[[]]
    answer1 = wfs(array, v, 2)
    answer2=[]
    dfs(array,[],2,answer2)
    print(answer1)
    print(answer2)
