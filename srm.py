#Student Record Management
students={} #It is used to store the database
students_id=[] #List to track the student ID
while True:
   print("/n1.Add Student Record")
   print("2.View all the students")
   print("Searching of the students")
   print("4.Update the students data")
   print("5.Delete the students data")
   print("6.Exit")

   choice=input("Enter the choice")

   if choice=='1':
      student_id=input("Enter the ID of the student : ")
      student_name=input("Enter the name of the student :")
      age=input("Enter the age of the student :")
      grade=input("Enter the grade of the student :")
      students[student_id]={'Name':student_name,'grade':grade,'age':age}
      students_id.append(students_id)
      print("Student added successfully!")
    
   elif choice == '2':  # View All Students
        if not students:
            print("No students found.")
        else:
            for student_id in student_id:
                student = students[student_id]
                print(f"ID: {student_id}, Name: {student['student_name']}, Age: {student['age']}, Grade: {student['grade']}")
   
   elif choice=='3':
       student_id=input("Enter student ID to search : ")
       if student_id in students :
           student=students[student_id]
           print(f"ID:{student_id}, name={student_name}, Age={age}, Grade={grade}")
       else:
           print("Student Not Found")
        
   elif choice=='4':
       student_id=input("Enter student_id to update")
       if student_id in students:
           student_name=input("Enter new name : ")
           age=input("enter new age : ")
           grade=input("Enter new grade : ")
           students[student_id]={'Name': student_name,'age': age,'grade':grade}
           print("Student data updated successfully")
       else:
           print("student not found.")
   elif choice == '5':  # Delete Student Record
        student_id = input("Enter student ID to delete: ")
        if student_id in students:
            del students[student_id]
            student_ids.remove(student_id)
            print("Student record deleted successfully!")
        else:
            print("Student not found.")
   elif choice == '6':  # Exit
        print("Exiting...")
        break
        
   else :
        print("Invalid choice. Please try again.")
    

                 

    
   
