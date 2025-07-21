# # Student Information
name = input("Enter your Name: ")
father = input("Enter your Father Name: ")

# Marks Input
marks = int(input("Enter the student marks: "))

# Eligibility Check
if marks >= 70:
    print("\n✅ You are eligible for admission!")
    print("Select your Group:")
    print("1. Pre-Engineering")
    print("2. Pre-Medical")

    group = int(input("Enter Group Number (1 or 2): "))
    selected_group = ""

    if group == 1:
        selected_group = "Pre-Engineering"
        print("\nSubjects Options for Pre-Engineering:")
        print("1. English, Biology, Urdu, Chemistry, Physics")
        print("2. English, Biology, Urdu, Math, Physiology")
    elif group == 2:
        selected_group = "Pre-Medical"
        print("\nSubjects Options for Pre-Medical:")
        print("1. Mathematics, English, Urdu, Physics, Chemistry, Islamiyat")
        print("2. Mathematics, English, Urdu, Chemistry, Pakistan Studies")
    else:
        print("❌ Invalid group selected.")
        exit()

    subject_option = int(input("Select Subject Option (1 or 2): "))

    # Subject Selection Based on Group
    if group == 1:
        if subject_option == 1:
            subjects = "English, Biology, Urdu, Chemistry, Physics"
        elif subject_option == 2:
            subjects = "English, Biology, Urdu, Math, Physiology"
        else:
            print("❌ Invalid subject option.")
            exit()
    elif group == 2:
        if subject_option == 1:
            subjects = "Mathematics, English, Urdu, Physics, Chemistry, Islamiyat"
        elif subject_option == 2:
            subjects = "Mathematics, English, Urdu, Chemistry, Pakistan Studies"
        else:
            print("❌ Invalid subject option.")
            exit()

    # Final Admission Slip
    print("\n🎓 Your Admission Slip")
    print("------------------------")
    print("Name           :", name)
    print("Father Name    :", father)
    print("Marks          :", marks)
    print("Selected Group :", selected_group)
    print("Subjects       :", subjects)
    print("Status         : ✅ Admission Confirmed")
    print("------------------------")

else:
    print("\n❌ You are not eligible for admission. Try next time.")
