#produce 5 cubes

n = int(input("number: "))

if n < 1:
    print("Invalid input, Enter a number greater than 0.")
else:
    total = 0

    for i in range(1, n + 1):
        cube = i ** 3
        print(cube)
        total = total + cube

    print("cubes total:", total)