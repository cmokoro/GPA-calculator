# Chidi Okoro
# July 24 2022
# Comp 163-001


# Imports module for apllication rules.

import gpa_calc_rules

#This code creates a gpa functions.
def gpa(credits,points):
    gpa = points / credits

    return gpa 



#This code declares variables.
GPA_points = 0
GPA_credits = 0
total_credits = 0
total_points = 0.0

s_major_points = 0
major_points = 0
major_credits = 0

#This code outputs welcome statement and rules for what the program does.

print(f"{'Welcome to The GPA Calculator!' : ^10}")
print(" ")
print(gpa_calc_rules.rules())
print(" ")
user_name = input("Enter your name: ")
print("")

#This code uses a user input in a for loop of total semester and creates a semster course dictionary with class and grade.
semester_num = int(input("Enter total semesters completed: "))
for i in range(semester_num):
    print("semester ", i + 1)
    semester_gpa = 0
    semester_points = 0.0
    semester_credits = int(input("Enter total semester credit hours:"))
    total_credits += semester_credits
    major_credits += int(input("Enter total semester major credit hours:"))
    class_num = int(input("Enter Total number of classes: "))
    semester = {}
    
    class_grade = 0
    for i in range(class_num):
        class_name = input("Enter class name: ")
        class_grade = int(input("Enter class number grade: "))
        semester[class_name] = class_grade
       
    print(semester)
    print(" ")
    #This code is a for loop to calculate semester gpa
    semester_points = 0  
    for course, grade in semester.items():
        course_credits = int(input(f'Enter {course} credit hours: '))
        if grade >= 93:
            semester_points += (4.0 * course_credits)
            
        elif grade >= 90:
            semester_points += (3.7 * course_credits)

        elif  grade >= 87:
            semester_points += (3.3 * course_credits)
        
        elif grade >= 83:
            semester_points += (3.0 * course_credits)
        
        elif grade >= 80:
            semester_points += (2.7 * course_credits)

        elif grade >= 77:
            semester_points += (2.3 * course_credits)

        elif grade >= 73:
            semester_points += (2.0 * course_credits)

        elif grade>= 70:
            semester_points +=(1.7 * course_credits)
        
        elif grade >= 67:
            semester_points += (1.3 * course_credits)

        elif grade >= 65:
            semester_points += (1.0 * course_credits)

        else:
            semester_points += 0.0

        total_points += semester_points
        total_credits += course_credits

       


        #This code is a Major GPA conditional statements
        major_course_Y_N = input(f'Enter either yes or no if {course} is a major course:').lower()
        while major_course_Y_N == "yes":
            m_course_credits = course_credits

            if grade >= 93:
                s_major_points += (4.0 * m_course_credits)
            
            elif grade >= 90:
                s_major_points += (3.7 * m_course_credits)

            elif  grade >= 87:
                s_major_points += (3.3 * m_course_credits)
        
            elif grade >= 83:
                s_major_points += (3.0 * m_course_credits)
        
            elif grade >= 80:
                s_major_points += (2.7 * m_course_credits)

            elif grade >= 77:
                s_major_points += (2.3 * m_course_credits)

            elif grade >= 73:
                s_major_points += (2.0 * m_course_credits)

            elif grade>= 70:
                s_major_points +=(1.7 * m_course_credits)
        
            elif grade >= 67:
                s_major_points += (1.3 * m_course_credits)

            elif grade >= 65:
                s_major_points += (1.0 * m_course_credits)

            else:
                s_major_points += 0.0
            major_course_Y_N = " " 


#This code prints semester gpa.
    print("Semester GPA: ", f'{gpa(semester_credits, semester_points):.2f}')
    print(" ")




#This code lets user enter total passed credit hours and quality points.
print("Below enter your total passed credit hours and quality points: ")
total_points_earned = int(input("Enter total quality points earned: ")) 
total_credits_earned = int(input("Enter total credit hours earned: "))
        
    
        




    
   



#This code print major gpa, honors and regular gpa.
major_points += s_major_points
print("Major GPA: ", f'{gpa(major_credits,major_points):.2f}')
print("GPA:", f'{gpa(total_credits_earned,total_points_earned):.2f}')
print("Honors GPA: ", f'{gpa(total_credits,total_points):.2f}')

