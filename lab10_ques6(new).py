def get_grade(marks):
    if marks >= 80:
        return "A"
    elif marks >= 60:
        return "B"
    elif marks >= 40:
        return "C"
    else:
        return "F"

students = int(input())
grade = {}

for i in range(students):
    entry = input().split()
    student = entry[0]
    score = int(entry[1])
    
    res = get_grade(score)
    print(student + ":", res)
    
    if res in grade:
        grade[res] += 1
    else:
        grade[res] = 1

print("Grade count:")
print(grade)