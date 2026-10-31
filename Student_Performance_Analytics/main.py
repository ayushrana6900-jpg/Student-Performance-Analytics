# Student Performance Analytics Toolkit

student_data = {
    'S101': {'name': 'Adeeb', "marks": [85, 90, 78]},
    'S102': {'name': 'Ayush', "marks": [92, 88, 95]},
    'S103': {'name': 'Harshit', "marks": [78, 82, 89]}
}

def add_student(student_id, name, marks):
    if student_id in student_data:
        print(f"Student ID {student_id} already exists.")
    else:
        student_data[student_id] = {'name': name, 'marks': marks}
        print(f"Student {name} added successfully.")

    return student_data[student_id]


def total_marks(student_id):
    if student_id in student_data:
        total = sum(student_data[student_id]['marks'])
        return total
    else:
        print(f"Student ID {student_id} not found.")
        return None

def average_marks(student_id):
    if student_id in student_data:
        avg = sum(student_data[student_id]['marks']) / len(student_data[student_id]['marks'])
        return avg
    else:
        print(f"Student ID {student_id} not found.")
        return None

def grade(average):
    if average>=75:
        return "Distinction"
    elif average>=60 and average<75:
        return "First Division"
    elif average>=40 and average<60:
        return "Pass"
    else:
        return "Fail"

def report_card(student_id):
    if student_id in student_data:
        name = student_data[student_id]['name']
        marks = student_data[student_id]['marks']
        total = total_marks(student_id)
        avg = average_marks(student_id)
        student_grade = grade(avg)
        print("\n===== STUDENT PERFORMANCE REPORT =====")
        print(f"{student_id} | {name} | Marks: {marks}")
        print(f"Total Marks: {total} | Average Marks: {avg:.2f} | Grade: {student_grade}")

    else:
        print(f"Student ID {student_id} not found.")

    high_performers = list(filter(lambda student_id: average_marks(student_id) >= 75, student_data.keys()))
    high_performers_names = []
    for student_id in high_performers:
        high_performers_names.append(student_data[student_id]['name'])
    class_average = sum(average_marks(student_id) for student_id in student_data) / len(student_data)
    print("High Performers (Average >= 75):", high_performers_names)
    print(f"Class Average: {class_average:.2f}")


def main():
    while True:
        print("\n===== STUDENT PERFORMANCE ANALYTICS TOOLKIT =====")
        print("1. Add Student")
        print("2. Generate Report Card")
        print("3. Exit")
        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            student_id = input("Enter Student ID: ")
            name = input("Enter Student Name: ")
            marks = list(int(input("Enter marks: ").split()))
            add_student(student_id, name, marks)

        elif choice == '2':
            student_id = input("Enter Student ID for Report Card: ")
            report_card(student_id)

        elif choice == '3':
            break

        else:
            print("Invalid choice. Please try again.")

main()

