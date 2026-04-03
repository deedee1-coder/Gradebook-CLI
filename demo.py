# example test file you can run for points 1-4 only
# save as demo.py in the project root

from gradebook.service import (
    add_student,
    add_course,
    enroll,
    add_grade,
    list_students,
    list_courses,
    list_enrollments,
    compute_average,
    compute_gpa,
)

student_id = add_student("Dea")
add_course("CS101", "Intro to CS")
enroll(student_id, "CS101")
add_grade(student_id, "CS101", 95)
add_grade(student_id, "CS101", 85)

print(list_students())
print(list_courses())
print(list_enrollments())
print(compute_average(student_id, "CS101"))
print(compute_gpa(student_id))