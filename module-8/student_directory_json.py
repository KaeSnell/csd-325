# Mikaela Snell
# July 20th, 2025
# Module 8.2 Assingment: Student Directory JSON
# This program reads a JSON file and prints the student data. 
# It also allows the user to add or remove students from the JSON file.

import json

def open_file():
    try:
      with open('student.json', 'r') as f:
        data = json.load(f)
        return data
    except FileNotFoundError:
      print("The file student.json was not found.")
      exit()

# Create a function to print the student data
def print_student(data):
    for student in data:
        print(f"{student['F_Name']} {student['L_Name']}: Student ID = {student['Student_ID']}, Email = {student['Email']}\n")

# A student class in the same format as the student.json file
class NewStudent:
    def __init__(self, F_Name, L_Name, Student_ID, Email):
        self.F_Name = F_Name
        self.L_Name = L_Name
        self.Student_ID = Student_ID
        self.Email = Email

# A function to create a new student using the NewStudent class
def new_student():
    F_Name = input("Enter First Name: ")
    L_Name = input("Enter Last Name: ")
    Student_ID = input("Enter Student ID: ")
    Email = input("Enter Email: ")
    return NewStudent(F_Name, L_Name, Student_ID, Email)

# A function to add a new student to the student.json file
def add_student(data, new_student):
    data.append(new_student.__dict__)
    with open('student.json', 'w') as f:
        json.dump(data, f, indent=4)
        print("Student saved successfully. The student.json file has been updated.\n")

# A function to remove a student from the student.json file
def remove_student(data):
  print("Which student would you like to remove?")
  deleted_student = input("Enter Student ID: ")

  found = False

  for student in data:
      if student['Student_ID'] == deleted_student:
          data.remove(student)
          with open('student.json', 'w') as f:
              json.dump(data, f, indent=4)
          print("Student removed successfully. The student.json file has been updated.\n")
          print("")
          found = True
          break

  if not found:
      print(f"No student found with Student ID: {deleted_student}\n")
                
            
def main():
    data = open_file()
  
    print("Welcome to the Student Management System\n")
    print("Original Student List:\n")
    print_student(data)
    print("Here are the database options:")
  
    while True:
        print("1. Add New Student")
        print("2. Remove Student")
        print("3. Exit")
      
        choice = input("Enter your choice: ")
      
        if choice == '1':
            new_student_obj = new_student()
            print("")
            print(f"Here is {new_student_obj.F_Name}'s information:\n")
            print_student([new_student_obj.__dict__])

            print("Do you want to save this students information in the database?\n")
            save_choice = input("Enter 'y' for yes or 'n' for no: ")
            if save_choice.lower() == 'y':
                add_student(data, new_student_obj)
                print("Updated Student List:\n")
                print_student(data)
                continue
            else:
                print("Student information not saved.")
                print("")
                continue
              
        elif choice == '2':
            was_removed = remove_student(data)
            if was_removed:
                print("Updated Student List:\n")
                print_student(data)

        elif choice == '3':
            print("Exiting the program.")
            exit()
    
        else:
            print("Invalid choice. Please enter 1, 2 or 3.")
            print("")
            continue

if __name__ == "__main__":
    main()