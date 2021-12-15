# using max()
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)

print(max(student_scores))


# without using max()
student_scores = input("Input a list of student scores ").split()
print(student_scores)
max=0
for score in student_scores:
  if int(score) > max:
    max = int(score)

print(f"The highest score in the class is: {max}")      
