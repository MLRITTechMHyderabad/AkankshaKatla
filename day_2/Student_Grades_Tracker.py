"""
Created on Thu Apr  3 10:07:48 2025

@author: akank
"""

students = [
    ("Alice", [85, 90, 78, 92]),
    ("Bob", [60, 65, 70, 75]),
    ("Charlie", [40, 45, 50, 55]),
    ("David", [95, 100, 98, 92])
    ]
s_dict = {}
for i, j in students:
    s_dict[i] = j

print(s_dict)

# 1.	Calculate the average grade for a given student. 
name = input()
if name in s_dict:
    avg_grade = sum(s_dict[name]) / len(s_dict[name])
    print("Grade: ",avg_grade)
else:
    print("Student not found")

# 2. student with the highest average grade.

highest_avg = 0
top_student = ""
for k,v in s_dict.items():
    avg = sum(v) / len(v)
    if avg > highest_avg:
        highest_avg = avg
        top_student = i
print(top_student)

# number of students who have passed.
 
passed_count = 0
for i in s_dict:
    avg = sum(s_dict[i]) / len(s_dict[i])
    if avg >= 50:
        passed_count += 1
print(passed_count)