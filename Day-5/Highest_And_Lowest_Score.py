student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]

min_num = student_scores[0]
for i in student_scores:
    if i < min_num:
        min_num = i
print(f"Minimum number is {min_num}")

max_num = student_scores[0]
for i in student_scores:
    if i>max_num:
        max_num = i
print(f"Maximum number is {max_num}")
