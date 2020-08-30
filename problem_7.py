count, i, j = 10001, 5, 0
num_arr = [1, 3, 5]


def is_prime(num):
    if num > 1:
        for k in range(2, num):
            if num % k == 0:
                return False
            else:
                return True
    else:
        return False


while True:
    i += 1
    if j == count:
        print("10001st number is: ", num_arr[10000])
        break
    if is_prime(i):
        j += 1
        num_arr.append(i)
