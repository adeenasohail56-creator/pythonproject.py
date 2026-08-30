# Student Grade Checker
print("="*30)
print("   STUDENT GRADE CHECKER")
print("="*30)
student_name = input("Enter student name: ").strip().title()
student_marks = int(input("Enter student marks out of 100: "))
# 1. Marks validation
if student_marks < 0 or student_marks > 100:
    print("\nError: Marks must be between 0 to 100")
    
else:
    # 2. Grade and Remarks decide karo
    if student_marks >= 90:
        student_grade = "A+"
        remarks = "Outstanding! Excellent Work"
    elif student_marks >= 80:
        student_grade = "A"
        remarks = "Excellent! Keep it up"
    elif student_marks >= 70:
        student_grade = "B"
        remarks = "Good Job"
    elif student_marks >= 60:
        student_grade = "C"
        remarks = "Satisfactory"
    elif student_marks >= 50:
        student_grade = "D"
        remarks = "Need Improvement"
    else:
        student_grade = "F"
        remarks = "Fail - Work Harder"

    # 3. Final Result Card
    print("\n" + "="*30)
    print("        RESULT CARD")
    print("="*30)
    print(f"Student Name : {student_name}")
    print(f"Total Marks  : {student_marks} / 100")
    print(f"Grade        : {student_grade}")
    print(f"Status       : {'PASS' if student_grade != 'F' else 'FAIL'}")
    print(f"Remarks      : {remarks}")
    print("="*30)
