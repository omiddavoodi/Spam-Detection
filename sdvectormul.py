def multiply(v1, v2):
    l1 = len(v1)
    l2 = len(v2)
    if (l1 == 0 or l2 == 0):
        return None
    i = 0
    j = 0
    ret = 0
    while (i < l1 and j < l2):
        if v1[i][0] > v2[j][0]:
            j += 1
        elif v1[i][0] < v2[j][0]:
            i += 1
        else:
            ret += v1[i][1] * v2[j][1]
            i += 1
            j += 1

    return ret
