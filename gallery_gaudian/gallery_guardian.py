import numpy as np


def guardian(L, x, p):
    if len(x) > 0:
        if x[0]+1 >= L:
            p.append(L)
        else:
            position = x[0]+1
            p.append(position)
            i = 1
            while i < len(x) and abs(position-x[i]) <= 1:
                i += 1
            x = x[i:]
            guardian(L, x, p)


if __name__ == "__main__":
    L = 100
    x = [np.random.randint(100) for i in range(20)]
    x.sort()
    p=[]
    guardian(L, x, p)
    print(x)
    print(p)

