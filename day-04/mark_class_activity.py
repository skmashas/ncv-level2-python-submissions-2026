mark = int(input("enter your mark here :"))
while mark <0 or mark > 100:
    print("invalid mark")
    mark = int(input("enter your mark here:"))  

    
if mark >= 80 and mark <= 100:
print("passed with distinction")

elif mark >= 70 and mark <= 79:
print(" highy competent")

elif mark >=50 and mark <= 69:
print("competent")

elif mark <= 49:
print(" not yet competent")

    
mark = int(input("enter your mark here :"))
while mark != -1:
    mark = int(input("enter your mark here:"))