# Gradebook CLI

A simple command-line application to manage students, courses, and grades using Python.

This project lets you:
- add students
- create courses
- enroll students into courses
- assign grades
- calculate averages and GPA

All data is saved locally in a JSON file so you can easily see and verify everything.

---

## What this project actually does

Think of this like a small “school system” you run from the terminal.

You:
1. create students  
2. create courses  
3. enroll students into courses  
4. add grades  
5. calculate results  

Everything is stored here:

```

data/gradebook.json

```

---

## Project Structure (what each file is for)

```

gradebook/
│
├── main.py                 # Where you run commands from (CLI)
├── README.md
│
├── data/
│   └── gradebook.json     # Stores all your data
│
├── logs/
│   └── app.log            # Stores logs (what the app is doing)
│
├── scripts/
│   └── seed.py            # Creates example data automatically
│
├── tests/
│   └── test_service.py    # Tests for your functions
│
└── gradebook/
├── models.py          # Student, Course, Enrollment classes
├── service.py         # Main logic (add, enroll, grade, etc.)
├── storage.py         # Reads/writes JSON file
└── logger_config.py   # Logging setup

````

### Important idea

- `main.py` → what YOU run  
- `service.py` → what actually does the work  
- `storage.py` → saves everything  

---

## Requirements

- Python 3 installed

Check this:

```powershell
py --version
````

If it prints a version → you're good.

---

## Setup (do this once)

### 1. Open the project folder

```powershell
cd path\to\gradebook
```

Make sure you see `main.py` inside.

---

### 2. Create a virtual environment

```powershell
py -m venv .venv
```

This creates an isolated Python environment.

---

### 3. Activate it

```powershell
.venv\Scripts\Activate.ps1
```

You should now see:

```
(.venv)
```

---

### 4. Dependencies

You don’t need to install anything — everything is built-in.

---

## Quick Start (fastest way to see it working)

Run:

```powershell
py scripts/seed.py
py main.py list students
```

This will:

* automatically create test data
* show students immediately

---

## Initialize Sample Data (important)

Instead of manually creating everything, you can generate example data.

```powershell
py scripts/seed.py
```

### What this actually does

It automatically creates:

* students
* courses
* enrollments
* grades

and saves them into:

```
data/gradebook.json
```

### When to use this

Use it if:

* you want to test quickly

Do NOT use it if:

* you want to build everything manually

---

## How to Use the Project (real usage)

All commands follow this format:

```powershell
py main.py <command> [options]
```

---

## Step-by-step usage

### 1. Add a student

```powershell
py main.py add-student --name "Dea"
```

Output:

```
Student added. ID: 1
```

What happened:

* student created
* ID automatically assigned

---

### 2. Add a course

```powershell
py main.py add-course --code CS101 --title "Intro to CS"
```

Output:

```
Course added.
```

---

### 3. Enroll student in course

```powershell
py main.py enroll --student-id 1 --course CS101
```

Output:

```
Enrollment added.
```

What happened:

* student is now linked to that course

---

### 4. Add a grade

```powershell
py main.py add-grade --student-id 1 --course CS101 --grade 90
```

Output:

```
Grade added.
```

---

### 5. View data

#### Students

```powershell
py main.py list students
```

#### Sorted students

```powershell
py main.py list students --sort name
py main.py list students --sort id
```

---

#### Courses

```powershell
py main.py list courses
```

---

#### Enrollments

```powershell
py main.py list enrollments
```

Example output:

```
Student ID: 1, Course: CS101, Grades: [90]
```

---

### 6. Calculate average

```powershell
py main.py avg --student-id 1 --course CS101
```

Output:

```
Average: 90.00
```

---

### 7. Calculate GPA

```powershell
py main.py gpa --student-id 1
```

Output:

```
GPA: 90.00
```

---

## Example full workflow

```powershell
py main.py add-student --name "Dea"
py main.py add-course --code CS101 --title "Intro to CS"
py main.py enroll --student-id 1 --course CS101
py main.py add-grade --student-id 1 --course CS101 --grade 90
py main.py add-grade --student-id 1 --course CS101 --grade 80
py main.py avg --student-id 1 --course CS101
py main.py gpa --student-id 1
```

---

## Logging (what it records)

The app logs activity here:

```
logs/app.log
```

It records:

* when data is loaded/saved
* errors

---

## Running tests

```powershell
py -m unittest tests/test_service.py
```

If everything is correct:

* all tests pass

---

## Design Decisions

* JSON instead of database → simpler and visible
* Separate files → easier to understand
* CLI → practice real-world tools
* auto IDs → avoids mistakes

---

## Limitations

* no delete/update
* no database
* GPA is simple average
* basic validation only

---

## Final Note

This project focuses on learning:

* structure
* clarity
* real-world workflow

It’s designed to be simple but complete.
