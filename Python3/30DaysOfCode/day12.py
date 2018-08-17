# class Person:
#     def __init__(self, firstName, lastName, idNumber):
#         self.firstName = firstName
#         self.lastName = lastName
#         self.idNumber = idNumber
#     def printPerson(self):
#         print("Name:", self.lastName + ",", self.firstName)
#         print("ID:", self.idNumber)

class Student(Person):
    #   Class Constructor
    #   
    #   Parameters:
    #   firstName - A string denoting the Person's first name.
    #   lastName - A string denoting the Person's last name.
    #   id - An integer denoting the Person's ID number.
    #   scores - An array of integers denoting the Person's test scores.
    #
    # Write your constructor here
    def __init__(self,firstName,lastName,idNumber,scores):
        Person.__init__(self,firstName, lastName,idNumber)
        self.scores = scores

    #   Function Name: calculate
    #   Return: A character denoting the grade.
    #
    # Write your function here
    def calculate(self):
        myAverage = sum(self.scores) / float(len(self.scores))
        if myAverage >= 90 and myAverage <=100:
            grade = "O"
        elif myAverage >= 80 and myAverage <90:
            grade = "E"
        elif myAverage >= 70 and myAverage <80:
            grade = "A"
        elif myAverage >= 55 and myAverage <70:
            grade = "P"
        elif myAverage >= 40 and myAverage <55:
            grade = "D"
        elif myAverage <40:
            grade = "T"
        return grade

# line = input().split()
# firstName = line[0]
# lastName = line[1]
# idNum = line[2]
# numScores = int(input()) # not needed for Python
# scores = list( map(int, input().split()) )
# s = Student(firstName, lastName, idNum, scores)
# s.printPerson()
# print("Grade: ", s.calculate())