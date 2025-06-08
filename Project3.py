# Student Record System
# Objective: Manage full student profiles.
# Features:
# • Store student name, age, marks.
# • Add, update, delete student records.
# • Display all students in formatted view.

L=[]
def add_student():
    name=input("Enter Student name:")
    age=int(input("Enter Student age:"))
    marks=float(input("Enter student marks:"))
    student={"name":name,"age":age,"marks":marks}
    print(student)
    L.append(student)
    print("student added")
def update_student(L):
    search_name=input("Enter student name to update:")
    for student in L:
        if search_name==student['name']:
            student['name']=input("Enter new name:")
            new_age=int(input("Enter new age:"))
            new_marks=float(input("Enter new marks:"))
            if new_age:
                student['age']=new_age
            if new_marks:
                student['marks']=new_marks
            break

def delete_student(L):
    name_to_delete=input("Enter student name to delete:")
    for student in L:
        if student['name']==name_to_delete:
            L.remove(student)
            print("Student removed")
    
def display_student(L):
    print("\n--Student Records--")
    if (len(L)!=0):
        for i,student in enumerate(L,1):
            print(f"\nStudent {i}")
            print(f"Name:{student['name']}")
            print(f"Age:{student['age']}")
            print(f"Marks:{student['marks']}")
    else:
        print("NO STUDENT DETAILS FOUND")

def main():
    
    while True:
        print("Student record system")
        print("1.Add Student")
        print("2.Update Student")
        print("3.Delete Student")
        print("4.Display Students")
        print("5.Exit...")
        choice=input("Enter your choice(1-5)")
        if choice=="1":
            add_student()
        elif choice=="2":
            update_student(L)
        elif choice=="3":
            delete_student(L)
        elif choice=="4":
            display_student(L)
        else:
            print("Exiting....")
            break
        

main()