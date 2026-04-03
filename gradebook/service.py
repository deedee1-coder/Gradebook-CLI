from .models import Student, Course, Enrollment
from .storage import load_data, save_data


def add_student(name):
    """Add a new student and return the new id."""
    data = load_data()

    new_id = 1
    if data["students"]:
        new_id = max(student["id"] for student in data["students"]) + 1

    student = Student(new_id, name)

    data["students"].append({
        "id": student.id,
        "name": student.name
    })

    save_data(data)
    return student.id


def add_course(code, title):
    """Add a new course."""
    data = load_data()

    if any(course["code"] == code for course in data["courses"]):
        raise ValueError("course code already exists")

    course = Course(code, title)

    data["courses"].append({
        "code": course.code,
        "title": course.title
    })

    save_data(data)


def enroll(student_id, course_code):
    """Enroll a student in a course."""
    data = load_data()

    student_exists = any(student["id"] == student_id for student in data["students"])
    if not student_exists:
        raise ValueError("student not found")

    course_exists = any(course["code"] == course_code for course in data["courses"])
    if not course_exists:
        raise ValueError("course not found")

    already_enrolled = any(
        enrollment["student_id"] == student_id and enrollment["course_code"] == course_code
        for enrollment in data["enrollments"]
    )
    if already_enrolled:
        raise ValueError("student is already enrolled in this course")

    enrollment = Enrollment(student_id, course_code, [])

    data["enrollments"].append({
        "student_id": enrollment.student_id,
        "course_code": enrollment.course_code,
        "grades": enrollment.grades
    })

    save_data(data)


def add_grade(student_id, course_code, grade):
    """Add a grade to a student's enrollment."""
    data = load_data()

    if not isinstance(grade, (int, float)):
        raise TypeError("grade must be a number")
    if grade < 0 or grade > 100:
        raise ValueError("grade must be between 0 and 100")

    for enrollment in data["enrollments"]:
        if enrollment["student_id"] == student_id and enrollment["course_code"] == course_code:
            enrollment["grades"].append(grade)
            save_data(data)
            return

    raise ValueError("enrollment not found")


def list_students(sort_by="name"):
    """Return all students sorted by name or id."""
    data = load_data()

    if sort_by == "name":
        return sorted(data["students"], key=lambda student: student["name"].lower())
    if sort_by == "id":
        return sorted(data["students"], key=lambda student: student["id"])
    return data["students"]


def list_courses(sort_by="code"):
    """Return all courses sorted by code or title."""
    data = load_data()

    if sort_by == "code":
        return sorted(data["courses"], key=lambda course: course["code"].lower())
    if sort_by == "title":
        return sorted(data["courses"], key=lambda course: course["title"].lower())
    return data["courses"]


def list_enrollments():
    """Return all enrollments sorted by student_id and course_code."""
    data = load_data()
    return sorted(
        data["enrollments"],
        key=lambda enrollment: (enrollment["student_id"], enrollment["course_code"])
    )


def compute_average(student_id, course_code):
    """Compute average grade for one student's course enrollment."""
    data = load_data()

    for enrollment_item in data["enrollments"]:
        if (
            enrollment_item["student_id"] == student_id
            and enrollment_item["course_code"] == course_code
        ):
            grades = enrollment_item["grades"]
            if not grades:
                return 0
            return sum(grades) / len(grades)

    raise ValueError("enrollment not found")


def compute_gpa(student_id):
    """Compute simple GPA as the mean of course averages."""
    data = load_data()

    course_averages = []

    for enrollment_item in data["enrollments"]:
        if enrollment_item["student_id"] == student_id and enrollment_item["grades"]:
            avg = sum(enrollment_item["grades"]) / len(enrollment_item["grades"])
            course_averages.append(avg)

    if not course_averages:
        return 0

    return sum(course_averages) / len(course_averages)