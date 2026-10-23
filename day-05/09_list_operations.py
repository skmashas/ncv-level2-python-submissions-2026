# LIST



marks = []
i = 0
mark =int(input("enter mark(or -1 to stop)"))

while mark != -1:
    marks.append(mark)
    i += 1
    mark =int(input("enter mark(or -1 to stop)"))
              
print(f"Our list has {len(marks)} elements")

for x in range(len(marks)):
    print(f"mark{x+1} is {marks[x]}",end="| ")
# get the average of all marks
total = 0
for x in range(len(marks)):
    mark = marks[x]
    total = total+mark
    
avg = total / len(marks)
print(f"The average of all marks = {avg}")