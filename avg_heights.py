# without using len(), sum()

student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

sum=0
length=0
for height in student_heights:
  sum+=height
  length+=1
print(round(sum/length))

#using len(), sum()
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

print(round(sum(student_heights)/len(student_heights)))
