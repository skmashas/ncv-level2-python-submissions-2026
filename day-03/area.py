import math
area = float(input("Area (square metres): "))
if area <= 0:
    print("The area must be greater than zero.")
else:
    side = math.sqrt(area)
    print(f"Side: {side:.2f} m")
