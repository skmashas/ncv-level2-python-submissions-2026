import math
x = float(input("x: "))
y = float(input("y: "))
hyp = math.pow((x), 2) + math.pow((y), 2)
if x <= 0:
    print("x must be greater than zero.")
else:
    if y <= 0:
        print("y must be greater than zero.")
    else:
        r = math.sqrt(math.pow((x), 2) + math.pow((y), 2))
        print(f"r: {r:.2f} m")
