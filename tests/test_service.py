import os
import unittest

from gradebook.service import (
    add_student,
    add_course,
    enroll,
    add_grade,
    compute_average,
)
from gradebook.storage import save_data


class TestService(unittest.TestCase):
    def setUp(self):
        os.makedirs("data", exist_ok=True)
        save_data({
            "students": [],
            "courses": [],
            "enrollments": []
        })

    def test_add_student(self):
        student_id = add_student("Dea")

        self.assertEqual(student_id, 1)

    def test_add_grade(self):
        student_id = add_student("Dea")
        add_course("CS101", "Intro to CS")
        enroll(student_id, "CS101")

        add_grade(student_id, "CS101", 95)

        average = compute_average(student_id, "CS101")
        self.assertEqual(average, 95)

    def test_compute_average_happy_path(self):
        student_id = add_student("Ana")
        add_course("PY101", "Python Basics")
        enroll(student_id, "PY101")
        add_grade(student_id, "PY101", 80)
        add_grade(student_id, "PY101", 100)

        average = compute_average(student_id, "PY101")

        self.assertEqual(average, 90)

    def test_compute_average_edge_case_no_grades(self):
        student_id = add_student("Ylli")
        add_course("DB101", "Databases")
        enroll(student_id, "DB101")

        average = compute_average(student_id, "DB101")

        self.assertEqual(average, 0)


if __name__ == "__main__":
    unittest.main()