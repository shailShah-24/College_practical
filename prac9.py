# 20CE134 Shail shah
# GITHUB LINK : https://github.com/shailShah-24/College_practical.git
#Consider an example of declaring the examination result. Design three classes: Student, Exam, and Result. The Student class has data members such as those representing rollNumber, Name, etc. Create the class Exam by inheriting Student class. The Exam class adds fields representing the marks scored in six subjects. Derive Result from the Exam class, and it has its own fields such as total_marks. Write an interactive program to model this relationship.

class Student:
    def __init__(self):  # initialize constructor
        self.name = ""
        self.rollNo = 0

    def takeStudentData(self):  # take input from user
        self.name = input("Enter the name of student : ")
        print("Enter the roll number of", self.name, ": ", end="")
        self.rollNo = input()

    def StudentData(self):  # print the student data
        print("\nStudent name is", self.name)
        print("Roll number of", self.name, "is", self.rollNo)


class Exam(Student):  # multilevel inheritance
    def __init__(self):  # initialize constructor
        Student.__init__(self)
        self.arr = []

    def takeInput(self):  # take input from user
        for i in range(0, 6):
            print("Enter the marks of subject", i + 1, ":", end=" ")
            n = int(input())
            self.arr.append(n)

    def printData(self):  # print the marks
        print(self.name, "Your marks is ", end="")
        print(self.arr)


class Result(Exam):  # multilevel inheritance
    def __init__(self):  # initialize constructor
        Exam.__init__(self)
        self.total_marks = 0

    def calculateAvg(self):  # print the average of marks
        self.check = True
        for i in range(0, 6):
            if (self.arr[i] < 33):  # if marks is < 33 no need to print average of marks
                print(self.name, "you are fail in subject:", i + 1)
                self.check = False
                break
            self.total_marks = self.total_marks + self.arr[i]

        if (self.check):
            print("Total marks is", self.total_marks)
            print(self.name, "You get", self.total_marks / 6, "%")


st = Student()
exam = Exam()
result = Result()

result.takeStudentData()
result.takeInput()

result.StudentData()
result.printData()
result.calculateAvg()