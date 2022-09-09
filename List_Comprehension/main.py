# numbers = [1,2,3]
#
# new_list = [number+1 for number in numbers]
# print(new_list)
# #output is [2, 3, 4]

# new_list = [number*2 for number in range(1,5)]
#
# print(new_list)
import random

names = {
    "students": ["aravind", "hari", "sai", "dinesh"],
    "marks": [60, 50, 70, 90]
}

import pandas

names_df = pandas.DataFrame(names)
# print(names_df)
#
# for (key,value) in names_df.items():
#     print(value)

for (index, row) in names_df.iterrows():
    print(row.marks)

#
# new_names = [name for name in names if len(name)>4]
# print(new_names)
# #sol: ['aravind', 'dinesh']
#
# random_scores = {student: random.randint(1, 100) for student in names}
# print(random_scores)
#
# passed_students = {student: marks for (student, marks) in random_scores.items() if marks > 60}
# print(passed_students)
