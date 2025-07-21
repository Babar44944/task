Name = input("Enter Your Namne: ")
father =  input("Enter Your Father name: ")
# print(Name, father, 'Thank You')

marks = int(input("Enter Marks(0-100): "))

if marks >= 70:
    print("\n Your are Able: ")
    print("\n1.Pri-Engring \n2.Pri-Medical")
    
    Student_group = int(input("Enter your Group (1 or 2): "))
    Student_group = ""

    if Student_group == 1:
        selected_group = "Pre-Engineering"
        print(" ==> select your Subject\n----------------------------- ")
        print("1.Math English Physics Urdu Pakistan Study ")
        print("2.Math English Chemstry Urdu Pakistan Stud\n ")
        
        sub_1 = int(input(" ==> Select Your Option (1 or 2): "))
        
        if sub_1 == 1:
            print("You selected: Math, English, Physics, Urdu, Pakistan Study")
        elif sub_1 == 2:
            print("2.Math English Chemstry Urdu Pakistan Stud")
        else:
            print("ERROR")   
   
    elif Student_group == 2:
        selected_group = "Pre-Medical"
        print("\n select you Subject \n 1.Biology Zology English Urdu Pakistan Study Chemistry \n 2.Biology Zology English Urdu botany Physice ")

        sub_2 = int(input("\n Select your option (1 or 2): "))
        if sub_2 == 1:
            print("1.Biology Zology English Urdu Pakistan Study Chemistry")
        elif sub_2 == 2:
            print("2.Biology Zology English Urdu botany Physice")
        else:
            print("ERROR")
else:
    marks <= 70
    print("You are not Able")

print("\n==> NOW TIMING SHIFT<== \n")

shift = int(input("====> Select Shift <==== \n 1.Morining \n 2.Evening \n 3.Night \n \n ===> [1 2 or 3] <=== :\n "))
if shift == 1:
    print("Morining")
elif shift == 2:
    print("Evening")
elif shift == 3:
    print("Night")
else:
    print("ERROR")

print("\n Your Admission Slip")
print("------------------------")
print("Name           :", Name)
print("Father Name    :", father)
print("Marks          :", marks)
print("Selected Group :", Student_group, sub_1 , sub_2)
print("Subjects       :", sub_1)
print("Shift          :", shift)
print("Status         : Admission Confirmed")
print("------------------------")