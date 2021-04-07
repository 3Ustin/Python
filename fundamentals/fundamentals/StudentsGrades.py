import types
"""
How many students will be added to the list?
    - 2-8
How will the program know?
    - input stored into variable
What does the program need to know for each student?
    - name, grade, course
How will the program keep track of the students?
    - List of directories
How will the program display the students after all of them are added?
    - print.
"""

studentList = [[],[],[]]
#IDEAL FOR SITUATION
# studentList = [{"name": "Austin",}{}{}]

print(studentList)
def studentInput():
    print("How many students?")
    studentNum = input() #How many student?
    for n in range(0,int(studentNum)):
        #ASKING FOR NAME
        print("Name:") 
        studentList[0].append(input())  # name of student?
        while studentList[0][n].isdecimal():
            print("error enter a name:")
            studentList[0][n] = input()
        #ASKING FOR GRADE
        print("Grade:") 
        studentList[1].append(input())
        while studentList[1][n].isdecimal() == False:
            print("error enter a grade:")
            studentList[1][n] = input()
        #ASKING FOR COURSE
        print("Course: 0-Math, 1-Science,2-History") 
        studentList[2].append(input())
        print(f"This is the outside test{studentList[2][n].isdecimal()}")
        while (studentList[2][n].isdecimal() == False or studentList[2][n] != "0" and studentList[2][n] != "1" and studentList[2][n] != "2"):
            print(f"This is the inside test{studentList[2][n].isdecimal()}")
            print("error enter a Course: 0-Math, 1-Science,2-History")
            studentList[2][n] = input()
    for i in range(0,studentNum):
        print()
        for j in range(0,):
studentInput()