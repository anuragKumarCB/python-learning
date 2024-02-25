# Problem: Assign a letter grade based on a student's score:
# A (90-100), B (80-89), C (70-79), D (60-69), F (below 60).

# take score from student and convert it to integer
student_score = input("Please enter your score : ")
student_score_in_int = int(student_score)

# (condition for grading)

# check for invalid score
if student_score_in_int < 0 or student_score_in_int > 100:
    print("Please enter valid score between 0-100")

elif student_score_in_int >= 90:
    grade = "A"
    
elif student_score_in_int >= 80:
    grade = "B"

elif student_score_in_int >= 70:
    grade = "C"

elif student_score_in_int >= 60:
    grade = "A"

else:
    grade = "A"

print("Grade -",grade)