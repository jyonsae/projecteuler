number = 0
sum_of_numbers = 0
repeat = 1000

while number < repeat:
    if number % 3 == 0 or number % 5 == 0:
        sum_of_numbers += number
    number += 1

print(sum_of_numbers)
