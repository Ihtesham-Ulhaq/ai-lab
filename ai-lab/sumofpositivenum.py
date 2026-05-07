def sum_of_positives(numbers):
    total = 0
    for num in numbers:
        if num > 0:
            total += num
    return total


print(sum_of_positives([1, 4, 7, 12]))
