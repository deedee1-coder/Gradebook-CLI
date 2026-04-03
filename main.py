import argparse
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


def main():
    parser = argparse.ArgumentParser(description="Gradebook CLI")
    subparsers = parser.add_subparsers(dest="command")

    parser_add_student = subparsers.add_parser("add-student", help="Add a new student")
    parser_add_student.add_argument("--name", required=True, help="Student name")

    parser_add_course = subparsers.add_parser("add-course", help="Add a new course")
    parser_add_course.add_argument("--code", required=True, help="Course code")
    parser_add_course.add_argument("--title", required=True, help="Course title")

    parser_enroll = subparsers.add_parser("enroll", help="Enroll student in course")
    parser_enroll.add_argument("--student-id", required=True, type=int, help="Student ID")
    parser_enroll.add_argument("--course", required=True, help="Course code")

    parser_add_grade = subparsers.add_parser("add-grade", help="Add grade")
    parser_add_grade.add_argument("--student-id", required=True, type=int)
    parser_add_grade.add_argument("--course", required=True)
    parser_add_grade.add_argument("--grade", required=True, type=float)

    parser_list = subparsers.add_parser("list", help="List data")
    parser_list.add_argument(
        "item",
        choices=["students", "courses", "enrollments"],
        help="What to list"
    )
    parser_list.add_argument("--sort", help="Sort field")

    parser_avg = subparsers.add_parser("avg", help="Compute average")
    parser_avg.add_argument("--student-id", required=True, type=int)
    parser_avg.add_argument("--course", required=True)

    parser_gpa = subparsers.add_parser("gpa", help="Compute GPA")
    parser_gpa.add_argument("--student-id", required=True, type=int)

    args = parser.parse_args()

    if args.command is None:
        parser.print_help()
        return

    try:
        if args.command == "add-student":
            new_id = add_student(args.name)
            print(f"Student added. ID: {new_id}")

        elif args.command == "add-course":
            add_course(args.code, args.title)
            print("Course added.")

        elif args.command == "enroll":
            enroll(args.student_id, args.course)
            print("Enrollment added.")

        elif args.command == "add-grade":
            add_grade(args.student_id, args.course, args.grade)
            print("Grade added.")

        elif args.command == "list":
            if args.item == "students":
                sort_by = args.sort if args.sort else "name"
                students = list_students(sort_by=sort_by)

                if not students:
                    print("No students found.")
                else:
                    for student in students:
                        print(f"ID: {student['id']}, Name: {student['name']}")

            elif args.item == "courses":
                sort_by = args.sort if args.sort else "code"
                courses = list_courses(sort_by=sort_by)

                if not courses:
                    print("No courses found.")
                else:
                    for course in courses:
                        print(f"Code: {course['code']}, Title: {course['title']}")

            elif args.item == "enrollments":
                enrollments = list_enrollments()

                if not enrollments:
                    print("No enrollments found.")
                else:
                    for enrollment_item in enrollments:
                        print(
                            f"Student ID: {enrollment_item['student_id']}, "
                            f"Course: {enrollment_item['course_code']}, "
                            f"Grades: {enrollment_item['grades']}"
                        )

        elif args.command == "avg":
            average = compute_average(args.student_id, args.course)
            print(f"Average: {average:.2f}")

        elif args.command == "gpa":
            gpa_value = compute_gpa(args.student_id)
            print(f"GPA: {gpa_value:.2f}")

    except Exception as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()