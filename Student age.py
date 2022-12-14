# We will write program that asks user for age inputs then prints out the average age of the given numbers
# Don't use len() or sum() functions, instead try to replicate the solution with for loops
##########################################
student_age = input("Input a list of student age ").split()
for n in range(0, len(student_age)):
  student_age[n] = int(student_age[n])
##########################################


