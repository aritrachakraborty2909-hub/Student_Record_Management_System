# Student Record Management & Search System

## A. Title
**Student Record Management & Search System (B.Tech 5th Semester AI/ML Lab)**

## B. Objective
The primary objective of this project is to build a lightweight, Object-Oriented Student Record Management System in Python without relying on external data analysis libraries like Pandas or NumPy. The program demonstrates core software engineering practices including OOP design, modular architecture, basic algorithm implementation (loops and conditional logic), command-line argument processing, and basic file handling across TXT, CSV, and JSON file formats.

## C. Features
* **Student Entity Management:** Track attributes like Student ID, Name, Department, Semester, and Subject Marks.
* **Grade & Performance Metrics:** Calculate total marks, average marks, and determine pass/fail status per student.
* **Multi-Format File Support:** Load and save student records seamlessly using TXT, CSV, and JSON formats.
* **Basic Search & Filtering Logic:**
  * Search by Student ID
  * Search by Name (substring matching)
  * Search by Department
  * Condition-based filtering (e.g., finding students with average marks above a threshold)
* **Command-Line Interface (CLI):** Full control via execution flags using Python's built-in `argparse` module.

## D. Project Structure
The program is divided into 4 Python modules to enforce separation of concerns:

```text
Student_Record_Management_System/
│── student.py         # Defines the Student entity and individual student-level operations
│── file_handler.py    # Standalone utilities for reading/writing TXT, CSV, and JSON files
│── manager.py         # StudentManager class managing collections of Student objects
│── main.py            # Command-line interface and entry point for execution
│── README.md          # Project documentation and report
└── data/              # Directory for sample input/output files
    ├── students.txt
    ├── students.csv
    └── students.json
```

### Module Responsibilities
* **`student.py`:** Contains the `Student` class encapsulating student details and methods for total marks, average marks, pass/fail status, and updating marks.
* **`file_handler.py`:** Contains lower-level parsing logic using Python standard modules (`csv`, `json`, standard file I/O).
* **`manager.py`:** Contains the `StudentManager` class storing multiple `Student` instances and handling repository-level operations such as search algorithms and file orchestration.
* **`main.py`:** Parses CLI arguments, initializes manager instances, triggers search or data modification routines, and handles display outputs.

## E. Requirements
* **Python Version:** Python 3.7 or higher
* **External Dependencies:** None (Uses Python Standard Library modules only: `csv`, `json`, `argparse`, `sys`).

## F. How to Run

### Command Options
* `--file`: Path to input data file (*Required*)
* `--format`: File format (`txt`, `csv`, or `json`) (*Required*)
* `--search-id`: Search by exact Student ID (*Optional*)
* `--search-name`: Search by Name substring (*Optional*)
* `--search-dept`: Search by Department name (*Optional*)
* `--min-avg`: Filter students with an average mark greater than or equal to a specified float value (*Optional*)
* `--out`: Output file path to save updated records (*Optional*)

### Execution Examples

#### Working with CSV Files (Search by Department):
```bash
python main.py --file data/students.csv --format csv --search-dept "Computer Science"
```

#### Working with JSON Files (Condition Search on Average Marks):
```bash
python main.py --file data/students.json --format json --min-avg 75.0
```

#### Working with TXT Files (Search by Student ID and Save Output):
```bash
python main.py --file data/students.txt --format txt --search-id 101 --out data/output.txt
```

## G. Input and Output

### Input Formats
* **TXT (`students.txt`):** Comma-separated lines containing ID, Name, Department, Semester, Mark1, Mark2, Mark3.
* **CSV (`students.csv`):** Standard CSV table with header `Student ID, Name, Department, Semester, Subject1, Subject2, Subject3`.
* **JSON (`students.json`):** List of JSON objects with nested marks structures.

### Sample Terminal Output
```plaintext
--- Loaded Records ---
ID: 101 | Name: Rahul | Dept: Computer Science | Sem: 1 | Marks: [78, 82, 69] | Total: 229 | Avg: 76.33 | Status: Pass
ID: 102 | Name: Priya | Dept: Computer Science | Sem: 1 | Marks: [91, 87, 94] | Total: 272 | Avg: 90.67 | Status: Pass
ID: 103 | Name: Amit | Dept: Mathematics | Sem: 1 | Marks: [65, 71, 68] | Total: 204 | Avg: 68.00 | Status: Pass

--- Search Result (Dept: Computer Science) ---
ID: 101 | Name: Rahul | Dept: Computer Science | Sem: 1 | Marks: [78, 82, 69] | Total: 229 | Avg: 76.33 | Status: Pass
ID: 102 | Name: Priya | Dept: Computer Science | Sem: 1 | Marks: [91, 87, 94] | Total: 272 | Avg: 90.67 | Status: Pass
```

## H. OOP Concepts Used
* **Classes:** Defined `Student` (data object) and `StudentManager` (container/controller object).
* **Objects:** Instantiated unique `Student` instances for each record loaded from files.
* **Constructors:** Used `__init__()` methods to set initial state upon object creation.
* **Attributes:** Encapsulated state properties (`student_id`, `name`, `department`, `semester`, `marks`).
* **Instance Methods:** Implemented methods operating directly on object data (`calculate_total()`, `calculate_average()`, `get_result()`, `display_student()`, `update_marks()`).

## I. File Handling Concepts Used
* **TXT Handling:** Used standard `open()`, `readlines()`, and `write()` with `with open(...)` context managers to safely handle file resources.
* **CSV Handling:** Utilized standard `csv.reader` and `csv.writer` with explicit header row extraction and formatting.
* **JSON Handling:** Leveraged `json.load()` to parse JSON directly into Python lists/dictionaries and `json.dump()` with `indent=4` formatting to serialize objects back to disk.

## J. Searching Concepts Used
All search algorithms avoid high-level helper functions, relying purely on fundamental Python control structures:
* **Iteration:** Linear traversal over lists using `for` loops.
* **Filtering:** Explicit `if` block checks comparing attributes (e.g., checking if `s.student_id == search_id` or `s.calculate_average() >= threshold`).
* **Case-Insensitive String Matching:** Basic `.lower()` conversion with the `in` membership operator for flexible substring searches.

## K. Learning Outcome / Conclusion
Through this assignment, I reinforced foundational Object-Oriented Programming principles by cleanly separating single-entity representation from multi-object management. I gained practical experience building modular Python packages across multiple `.py` files and handling varied persistence formats (TXT, CSV, JSON) manually without relying on external libraries like Pandas. The primary challenge involved ensuring proper data conversion types (strings to integers/floats) and maintaining consistent error handling across varied CLI inputs.
