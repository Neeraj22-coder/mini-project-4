students = {
    "S101": {"name": "Aman", "marks": [78, 65, 88]},
    "S102": {"name": "Riya", "marks": [35, 72, 61]},
    "S103": {"name": "Rahul", "marks": [90, 85, 95]},
    "S104": {"name": "Neha", "marks": [45, 55, 60]},
    "S105": {"name": "Pankaj", "marks": [80, 75, 85]}
}
def calculate_total(marks):
    return sum(marks)
def calculate_average(marks):
    return sum(marks) / len(marks)
def get_grade(average):
    if average >= 75:
        return "Distinction"
    elif average >= 60:
        return "First Division"
    elif average >= 40:
        return "Pass"
    else:
        return "Fail"
def build_report(student_id, student, show_grade=True):
    marks = student["marks"]
    total = calculate_total(marks)
    average = calculate_average(marks)
    grade = get_grade(average)
    print("\nStudent ID:", student_id)
    print("Name:", student["name"])
    print("Marks:", marks)
    print("Total:", total)
    print("Average:", round(average, 2))
    if show_grade:
        print("Grade:", grade)
def get_top_students(records):
    return list(filter(
        lambda student: calculate_average(student["marks"]) >= 75,
        records.values()
    ))
def class_summary(*marks, **details):
    average = sum(marks) / len(marks)
    print("\nClass Summary")
    print("Title:", details.get("title", "Class Report"))
    print("Average:", round(average, 2))
def recursive_sum(n):
    if n == 0:
        return 0
    else:
        return n + recursive_sum(n - 1)
def scope_example():
    message = "This is a local variable"
    print("\nScope Example:", message)
print("===== STUDENT PERFORMANCE REPORT =====")
for student_id, student in students.items():
    build_report(student_id, student)
top_students = get_top_students(students)
top_names = list(map(lambda s: s["name"], top_students))
print("\nHigh Performers:", top_names)
all_averages = list(map(
    lambda s: calculate_average(s["marks"]),
    students.values()
))
class_average = sum(all_averages) / len(all_averages)
print("\nClass Average:", round(class_average, 2))
class_summary(80, 70, 90, title="Python Class Report")
print("\nRecursive Sum (1 to 5):", recursive_sum(5))
scope_example()