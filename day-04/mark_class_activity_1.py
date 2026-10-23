

mark = int(input("enter your mark here :"))
if mark <0 or mark > 100:
    print("invalid mark")
    int(input("enter your mark here:"))  

    

if mark >= 80 and mark <= 100:
    print("outstanding")

elif mark >= 70 and mark <= 79:
    print(" highy competent")

elif mark >=50 and mark <= 69:
    print("competent")

elif mark >= 40 and mark <= 49 :
    print(" not yet competent")

    
else :
    print("not achieved")