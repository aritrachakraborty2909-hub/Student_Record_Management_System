class Student:
    def __init__(self, student_id, name, department, semester, marks):
        self.student_id = str(student_id)
        self.name = name
        self.department = department
        self.semester = int(semester)
        # Expecting marks as a list of integers e.g., [78, 82, 69]
        self.marks = [int(m) for m in marks]

    def calculate_total(self):
        total = 0
        for mark in self.marks:
            total += mark
        return total

    def calculate_average(self):
        if not self.marks:
            return 0.0
        return self.calculate_total() / len(self.marks)

    def get_result(self):
        # Pass if every mark is >= 40 and average >= 40
        for mark in self.marks:
            if mark < 40:
                return "Fail"
        return "Pass" if self.calculate_average() >= 40 else "Fail"

    def update_marks(self, new_marks):
        self.marks = [int(m) for m in new_marks]

    def display_student(self):
        print(f"ID: {self.student_id} | Name: {self.name} | Dept: {self.department} | "
              f"Sem: {self.semester} | Marks: {self.marks} | "
              f"Total: {self.calculate_total()} | Avg: {self.calculate_average():.2f} | "
              f"Status: {self.get_result()}")