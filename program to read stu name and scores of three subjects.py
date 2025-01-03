#python program to read the student name and scores of three subjects and print the student report card
stu_name=input("Student Name:")
sub1=int(input("subject score 1:"))
sub2=int(input("subject score 2:"))
sub3=int(input("subject score 3:"))
total=0
avg=0
if sub1>=35 and sub2>=35 and sub3>=35:
    total=sub1+sub2+sub3
    avg=(total)/3
    print("total:",total)
    print("average:",avg)
    print("Congractulations you are passed....!")
    if avg>=90:
        print("Congractulations you have qualified with first....!")
    elif avg>=80:
        print("Congractulations you have qualified with second....!")
    else:
        print("Congractulations you have qualified with third....!")
else:
    print("Better luck next time and you are failed....!")