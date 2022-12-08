import requests
import json


class Student:
    id = 0

    def __init__(self, full_name, age, level, mobile_number):
        self.id = Student.id
        self.full_name = full_name
        self.age = age
        self.level = level
        self.mobile_number = mobile_number
        Student.id += 1


def registerStudent():
    print("To create the account:")
    full_name = input("Full Name:")
    age = int(input("Age:"))
    level = input("Level: \" A-B-C\"")
    mobile_number = input("Mobile Number:")

    # Check entry level correctly
    if level in ("A", "B", "C"):
        student = Student(full_name, age, level, mobile_number)
        student_dict = {
            "full_name": full_name,
            "age": age,
            "level": level,
            "mobile_number": mobile_number,
        }

        result = requests.post("http://staging.bldt.ca/api/method/build_it.test.register_student", data=student_dict)
        # Check if the Created was done correctly
        if result.status_code == 200:
            print("created successfully.")
        else:
            print("creatd failed ")
    else:
        print("level must be A,B or C. ")


def editStudentDetails():
    input_id = input("Enter ID Number to Update the account:")

    deatils = requests.get("http://staging.bldt.ca/api/method/build_it.test.get_student_details",params={"id": input_id})
    data = deatils.json()
    exist=data['code']

    # Check if the student's ID has been found until the update is completed
    if exist == 200:
        full_name = input("Full Name:")
        age = int(input("Age:"))
        level = input("Level. \"A-B-C\":")
        mobile_number = input("Mobile Number:")

        # Check entry level correctly
        if level in ("A", "B", "C"):
            student_dict = {
                "full_name": full_name,
                "age": age,
                "level": level,
                "mobile_number": mobile_number,
            }
            result = requests.put("http://staging.bldt.ca/api/method/build_it.test.edit_student"
                                  ,params={"id": input_id}, data=student_dict)
            # Check if the update was done correctly
            if result.status_code == 200:
                print("updated successfully.")
            else:
                print("updated failed ")
        else:
            print("level must be A,B or C. ")
    else:
        print("ID Number Not Exist.")


def deleteStudent():
    input_id = input("Enter ID Number to Delete the account:")
    account = requests.delete("http://staging.bldt.ca/api/method/build_it.test.delete_student",
                              params={"id": {input_id}})
    data=account.json()
    deleted=data['code']
    if deleted == 200:
        print("deleted successfully")
    else:
        print("deleted failed")


def studentInFile():
    students = requests.get("http://staging.bldt.ca/api/method/build_it.test.get_students")

    data_json = students.json()
    exist = data_json['code']
    data = data_json['data']

    if exist == 200:
        file = open("allStudentsDetails.txt", "w")
        for student in data:
            data_txet="id:"+student['id']+"\tfull_name:"+student['full_name']+"\tage:"+str(student['age'])\
                      +"\tmobile_number:"+student['mobile_number']+"\tlevel:"+student['level']+"\n"

            file.write(data_txet)
        file.close()
        print("Students details have been entered into the file.")



def studentDetailsInFile():
    input_id = input("Enter ID Number to storge account in file:")

    deatils = requests.get("http://staging.bldt.ca/api/method/build_it.test.get_student_details",
                           params={"id": {input_id}})
    data_json=deatils.json()
    exist = data_json['code']
    data = data_json['data']

    if exist == 200:
        data_txet="id:"+data['id']+"\tfull_name:"+data['full_name']+"\tage:"+str(data['age'])\
                  +"\tmobile_number:"+data['mobile_number']+"\tlevel:"+data['level']+"\n"
        file=open("studentDetails.txt","a")
        file.write(data_txet)
        file.close()
        print("The student's details have been entered into the file.")
    else:
        print("ID Number Not Exist.")



while (True):
    print("""
    1-Register new Student.
    2-Edit Student Details.
    3-Delete Student.
    4-Export Student to text file.
    5-Export Student details to text file.
    6-Exit.""")
    input_1 = int(input("     Enter the service number:"))


    if input_1 == 1:        # Register new Student.
        registerStudent()

    elif input_1 == 2:      # Edit Student Details.
        editStudentDetails()

    elif input_1 == 3:      # Delete Student.
       deleteStudent()

    elif input_1 == 4:      # Export Students to text file.
        studentInFile()

    elif input_1 == 5:      # Export Student details to text file.
        studentDetailsInFile()

    elif input_1 == 6:      # To Exit.
        exit("exit successfully.")
    else:
        print("index error...")
