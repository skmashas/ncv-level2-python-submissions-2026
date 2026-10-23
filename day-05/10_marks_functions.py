
def get_marks():
    marks = []
    print("\nEnter marks (-1 to stop capturing)")

    mark = int(input("Enter mark: "))

    while mark != -1:
        marks.append(mark)
        mark = int(input("Enter mark: "))

    return marks


def display_marks(marks):
    if len(marks) == 0:
        print("No marks have been captured.")
        return

    for x in range(len(marks)):
        print(f"Mark {x + 1} is {marks[x]}", end=" | ")
    print()


def count_marks(marks):
    print(f"Number of marks: {len(marks)}")


def get_average(marks):
    if len(marks) == 0:
        print("No marks available to calculate average.")
        return

    total = 0

    for x in range(len(marks)):
        total = total + marks[x]

    avg = total / len(marks)
    print(f"The average mark is {avg:.2f}")


def highest_mark(marks):
    if len(marks) == 0:
        print("No marks available.")
        return

    highest = marks[0]

    for x in range(len(marks)):
        if marks[x] > highest:
            highest = marks[x]

    print(f"The highest mark is {highest}")


#10
marks = []

choice = 0

while choice != -1:
    print("\n===== MARKS MENU =====")
    print("1. Enter marks")
    print("2. Check number of marks")
    print("3. Calculate average marks")
    print("4. Highest mark")
    print("-1. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        marks = get_marks()
        display_marks(marks)

    elif choice == 2:
        count_marks(marks)

    elif choice == 3:
        get_average(marks)

    elif choice == 4:
        highest_mark(marks)

    elif choice == -1:
        print("Exiting program. Goodbye!")

    else:
        print("Invalid choice. Please try again.")
