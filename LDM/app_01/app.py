from pymongo import MongoClient

connection_string ="mongodb://root:123456@127.0.0.1:27017/"

client =  MongoClient(connection_string)

db = client["SIS"]
student_collection  = db["Student"]

def add_student(fullname,age,classname):
    student_obj = {"fullname":fullname,"age":age,"classname":classname}
    student_collection.insert_one(student_obj)
    print("Inserted Student")

def list_student():
    students = student_collection.find()
    for s in students:
        print(f"Username: {s.get('fullname')}")
        print(f"Age: {s.get('age')}")
        print(f"ClassName: {s.get('classname')}")

def delete_student(fullname):
    student = student_collection.find({"fullname":fullname})
    if(student is not None):
        student_collection.delete_one({"fullname":fullname})
    else:
        print("Can not find student")

if __name__ == "__main__":
    print("Enter a number ")
    print("1. Add Student")
    print("2. Delete Student")
    print("3. List Student")

    while True:
        choice = input("Please enter a number 0 to 9: ")
        if(choice =='1'):
            print("Add a student")
            fullname = input("Enter name: ")
            age = int(input("Enter age: "))
            class_name = input("Enter classname: ")
            add_student(fullname,age,class_name)
        if(choice =='2'):
            print("Delete a student")
            fullname = input("Enter a name ")
            delete_student(fullname)
        if(choice =='3'):
            print("List students")
            list_student()