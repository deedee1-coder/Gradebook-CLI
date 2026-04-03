class Student:
    """Represents a student."""

    def __init__(self, student_id, name):
        if not isinstance(student_id, int):
            raise TypeError("student_id must be an integer")
        if student_id <= 0:
            raise ValueError("student_id must be greater than 0")

        if not isinstance(name, str):
            raise TypeError("name must be a string")
        if not name.strip():
            raise ValueError("name cannot be empty")

        self.id = student_id
        self.name = name.strip()

    def __str__(self):
        return f"Student(id={self.id}, name='{self.name}')"


class Course:
    """Represents a course."""

    def __init__(self, code, title):
        if not isinstance(code, str):
            raise TypeError("code must be a string")
        if not code.strip():
            raise ValueError("code cannot be empty")

        if not isinstance(title, str):
            raise TypeError("title must be a string")
        if not title.strip():
            raise ValueError("title cannot be empty")

        self.code = code.strip()
        self.title = title.strip()

    def __str__(self):
        return f"Course(code='{self.code}', title='{self.title}')"


class Enrollment:
    """Represents a student's enrollment in a course."""

    def __init__(self, student_id, course_code, grades=None):
        if not isinstance(student_id, int):
            raise TypeError("student_id must be an integer")
        if student_id <= 0:
            raise ValueError("student_id must be greater than 0")

        if not isinstance(course_code, str):
            raise TypeError("course_code must be a string")
        if not course_code.strip():
            raise ValueError("course_code cannot be empty")

        if grades is None:
            grades = []

        if not isinstance(grades, list):
            raise TypeError("grades must be a list")

        for grade in grades:
            if not isinstance(grade, (int, float)):
                raise TypeError("each grade must be a number")
            if grade < 0 or grade > 100:
                raise ValueError("grades must be between 0 and 100")

        self.student_id = student_id
        self.course_code = course_code.strip()
        self.grades = grades

    def __str__(self):
        return (
            f"Enrollment(student_id={self.student_id}, "
            f"course_code='{self.course_code}', grades={self.grades})"
        )