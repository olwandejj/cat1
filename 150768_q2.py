class Student:
    def __init__(self, name):
        self.name = name
        self.grades = {}
    
    def addGrade(self, subject, grade):
        self.grades[subject] = grade

    def getAverageGrade(self):
        if not self.grades:
            return 0
        return sum(self.grades.values()) / len(self.grades)

class Classroom:
    def __init__(self):
        self.students = []
    
    def addStudent(self, student):
        self.students.append(student)
    
    def displayStudents(self):
        if not self.students:
            print("There are no students in the class.")
        else:
            for student in self.students:
                print(f"\nName: {student.name}, \nGrades: {student.grades}")
    
    def getStudentAverage(self, studentName):
        for student in self.students:
            if student.name.lower() == studentName.lower():
                return student.getAverageGrade()
        return None
    
    def getClassAverage(self, subject):
        total = 0
        count = 0
        for student in self.students:
            if subject in student.grades:
                total += student.grades[subject]
                count += 1
        if count == 0:
            return None
        return total / count


classroom = Classroom()


student1 = Student("James")
student1.addGrade("Computer Science", 85)
student1.addGrade("Physics", 90)

student2 = Student("Christine")
student2.addGrade("Computer Science", 78)
student2.addGrade("Physics", 82)

classroom.addStudent(student1)
classroom.addStudent(student2)


print("Displaying all students:")
classroom.displayStudents()


studentName = "James"
averageGrade = classroom.getStudentAverage(studentName)
if averageGrade is not None:
    print(f"\nThe average grade for {studentName} is {averageGrade}")
else:
    print(f"\n{studentName} not found.")


subject = "Computer Science"
classAverage = classroom.getClassAverage(subject)
if classAverage is not None:
    print(f"\nThe class average for {subject} is {classAverage}")
else:
    print(f"\nNo grades were found for {subject}.")
