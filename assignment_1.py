# Course Weight
Lab_weight = 20 / 6
Quizzes_weight = 15 / 6
Assignment_weight = 0.04
Midterms_weight = 0.125
Final_weight = 0.18
Preparation_weight = 0.06

# inputs
lab_completed = int(input("Enter the number of labs completed: "))
if lab_completed > 6:
  lab_completed = 6
quizzes_completed = int(input("Enter the number of quizzes completed: "))
if quizzes_completed > 6:
  quizzes_completed = 6
assignment1 = float(input("Enter the grade for assignment 1: "))
assignment2 = float(input("Enter the grade for assignment 2: "))
assignment3 = float(input("Enter the grade for assignment 3: "))
assignment4 = float(input("Enter the grade for assignment 4: "))
midterm1 = float(input("Enter the grade for midterm 1: "))
midterm2 = float(input("Enter the grade for midterm 2: "))
final_exam = float(input("Enter the grade for final exam 1: "))
prep_grade = float(input("Enter the grade for midterm and final preparation: "))

# Calculate total grade
lab_con = lab_completed * Lab_weight
quizzes_con = quizzes_completed * Quizzes_weight
assignment_con = (assignment1 + assignment2 + assignment3 + assignment4) * Assignment_weight
midterm_con = (midterm1 + midterm2) * Midterms_weight
final_con = final_exam * Final_weight
pre_con = prep_grade * Preparation_weight

total_grade = lab_con + quizzes_con + assignment_con + midterm_con + final_con + pre_con

# Output the final grade
print("Your grade is: ", round(total_grade))

