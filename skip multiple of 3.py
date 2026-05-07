def skip_multiples_of_3(N):
    for i in range(1, N + 1):
        if i % 3 == 0:
            continue
        print(i, end=" ")


skip_multiples_of_3(17)
