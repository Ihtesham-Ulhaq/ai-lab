def average_of_numbers():
    count = int(input("How many numbers? "))
    total = 0
    for i in range(count):
        num = float(input("Enter number: "))
        total += num
    avg = total / count
    print("Average =", avg)


average_of_numbers()
