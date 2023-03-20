students =[]
courses = []
marks = []



#input # of students 
print("Please tell me the number of students in the class :")
student_numbers = int(input())
#input number of courses 
print("How many courses are there: ")
course_numbers = int(input())





#input students info 
def StudentInfo():
    global student_numbers
    for i in range(student_numbers):
        student_id = input("Enter Students id : ")
        student_name = input("Enter Students name : ")
        student_DoB = input("Enter Students Dob : ") 
        students.append([student_id,student_name,student_DoB])
        


#input course information 
def CoursesInfo():
    global course_numbers
    for i in range(course_numbers):
        course_id = input("Enter course id : ")
        course_name = input("Enter course name : ") 
        courses.append([course_id,course_name])

#input course mark 
def CourseMark(): 
    global course_numbers
    for i in range(course_numbers):
        course_name = input("Name the course: ")
        if course_name not in courses[i][1]: 
            print("Course is not included")
        else: 
            for i in range(course_numbers):
                student_id = (input(" The id of student :"))
                mark = int(input("Enter student's mark: "))
                marks.append([student_id,mark])
#Courses List
def CourseList():
    global course_numbers
    print("Course List :")
    print("Course id\t||\tCourse Name")
    for i in range(course_numbers):
        print(courses[i][0],"\t\t||\t",courses[i][1])
    

#list students:
def StudentList():
    global course_numbers
    print("Student infomation : ")
    print("Student id\t||\tStudent Name\t||\tStudent DoB")
    for i in range(student_numbers):
        print(students[i][0],"\t||\t",students[i][1],"\t||\t",students[i][2])

#Mark for choosen course 
def MarkForEC():
    course_name = input("Name the course :")
    for i in range(course_numbers):
        if course_name not in courses[i][1]: 
            print("Course not included")
        else:
            print("Student id\t||\t Student Mark")
            for i in range(student_numbers):
                print(marks[i][0],"\t||\t",marks[i][1])






StudentInfo()
CoursesInfo()
o = 0
while o != 5:
    print("1. Show student list")
    print("2. Show course list")
    print("3. input course mark")
    print("4. show mark list for course ")
    print("5. Exit")
    o = int(input("Pick an option : "))
    if o == 1: 
        StudentList()
    elif o == 2:
        CourseList()
    elif o == 3: 
        CourseMark()
    elif o == 4: 
        MarkForEC()
    elif o == 5:
        print("Goodbye")
    else:
        print("That is not an option")