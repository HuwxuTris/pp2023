#Getting id name Dob Mark of Student

class Students: 
    def __init__(self,id,name,Dob):
        self.id = id
        self.name = name
        self.Dob = Dob
        self.__mark = []
    
    def Print(self):
        return self.id, self.name, self.Dob

# Getting id and name of course
class Courses: 
    def __init__(self,id,name):
        self.__id = id
        self.__name = name
    def Getinfo(self):
        return self.__id, self.__name
    def SetName(self):
        return self.__name
    def SetId(self):
        return self.__id 

class Marks:
    def __init__(self,student_id,mark):
        self.__student_id = student_id
        self.__mark = mark
    def Getinfo(self):
        return self.__student_id, self.__mark
    def SetSid(self):
        return self.__student_id
    def SetMark(self):
        return self.__mark
        
#function to print students info
def PrintStudentList(StudentList):
    print("Student infomation : ")
    print("Student id\t||\tStudent Name\t||\tStudent DoB")
    for Students in StudentList:
        print(f"{Students.id}\t||\t{Students.name}\t||\t{Students.Dob}")

def PrintCourseList(Courselist):
    print("Student infomation : ")
    print("Courses id\t||\tCourses Name")
    for Courses in CourseList:
        print(f"{Courses.SetId()}\t\t||\t{Courses.SetName()}")

def PrintMark(MarkList):
    for i in range(x): 
        Coursename = input("Input course's name : ")
        check = CourseList.count(Coursename)
        if check > 0:
            print("Course is not included")
        else:
            for Mark in MarkList:
                print("Student id\t||\tStudent Mark")
                print(f"{Mark.SetSid()}\t||\t{Mark.SetMark()}")
            
def MarkInput(Marklist):
    for i in range(x): 
        Coursename = input("Input course's name : ")
        check = CourseList.count(Coursename)
        if check > 0:
            print("Course is not included")
        else:
            for i in range(n):
                student_id = input("Enter Student id : ")
                mark = input("Student's mark for this course : ")
                a = Marks(student_id,mark)
                MarkList.append(a)

MarkList = []
StudentList = []
n = int(input("Input the number of student : "))
for i in range(n): 
    id = input("Enter Students id : ")
    name = input("Enter Students name : ")
    Dob = input("Enter Students Dob : ") 
    a = Students(id,name,Dob)
    StudentList.append(a)
CourseList = []
x = int(input("Input the number of courses : "))
for i in range(x):
    id = input("Enter Course id : ")
    name = input("Enter Course name : ")
    a = Courses(id,name) 
    CourseList.append(a)


o = 0
while o != 5:
    print("1. Show student list")
    print("2. Show course list")
    print("3. input course mark")
    print("4. show mark list for course ")
    print("5. Exit")
    o = int(input("Pick an option : "))
    if o == 1: 
        PrintStudentList(StudentList)
    elif o == 2:
        PrintCourseList(CourseList)
    elif o == 3:
        MarkInput(MarkList) 
    elif o == 4: 
        PrintMark(MarkList)
    elif o == 5:
        print("Goodbye")
    else:
        print("That is not an option")