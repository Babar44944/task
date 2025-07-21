Student_num = int(input("how many students grades they want to enter? "))
Student_list = []

for i in range(Student_num):
    
    print(f"\n ---Enter student {i+1} Info---")
    name = input("Enter Student Name : ")
    father = input("Enter Father Name :")
    marks =  int(input("Enter Your Marks  :"))
    
    if marks >= 90 and marks <= 100 :
        grade = "A"
    elif marks >= 80 and marks <= 90:
        grade = "B"
    elif marks >= 70 and marks <= 80:
        grade = "C"
    elif marks >= 60 and marks <= 70:
        grade = "D"
    else:
        grade = "Fail"
        
    print(f"\n ------Student result---- " )
    
    print("Student Name ========>", name)
    print("Student Father name =>", father)
    print("Student Marks =======>", marks)
    print("Student grade =======>", grade)
    
    # print(f'\n Name' [{name}] , f'n\ father'[{father}]) 