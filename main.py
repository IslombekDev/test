a = int(input('Enter a number: '))  # 5

while a != 1:
    counter = 2  # 2
    while counter <= a:
        if a % counter == 0:
            print(counter)
            a /= counter
            break
        counter += 1