from gradebook.storage import save_data


def main():
    data = {
        "students": [
            {"id": 1, "name": "Dea"},
            {"id": 2, "name": "Ana"},
            {"id": 3, "name": "Ylli"}
        ],
        "courses": [
            {"code": "CS101", "title": "Intro to CS"},
            {"code": "PY101", "title": "Python Basics"}
        ],
        "enrollments": [
            {
                "student_id": 1,
                "course_code": "CS101",
                "grades": [90, 85]
            },
            {
                "student_id": 2,
                "course_code": "CS101",
                "grades": [100, 95]
            },
            {
                "student_id": 3,
                "course_code": "PY101",
                "grades": [88, 92]
            }
        ]
    }

    save_data(data)
    print("Sample data saved to data/gradebook.json")


if __name__ == "__main__":
    main()