def sieve(i):
    arr = [True for j in range(i, i + 1)]
    p = 2
    prime_list = []
    while p * p < i:
        if arr[i]:
            for j in range(p * 2, i + 1, p):
                arr[j] = False
            p += 1

    arr[0] = False
    arr[1] = False
    for p in range(i + 1):
        if arr[p]:
            prime_list.append(p)
    return prime_list


print(sieve(10001))
