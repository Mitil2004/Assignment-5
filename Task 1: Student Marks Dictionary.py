# task_1.py
# This script demonstrates the use of a dictionary to store and retrieve student marks.

def find_student_marks():
    """
    Creates a dictionary of student marks, asks for a student's name,
    and displays their marks or a 'not found' message.
    """
    # 1. Create a dictionary of student names and marks.
    student_marks = {
        'Alice': 85,
        'Bob': 92,
        'Charlie': 78,
        'Diana': 95,
        'Eve': 88
    }

    # 2. Ask the user to input a student's name.
    student_name = input("Enter the student's name: ")

    # 3. Retrieve and display the marks using the .get() method.
    # .get() is used to avoid an error if the key is not found.
    # It returns None by default if the key doesn't exist.
    marks = student_marks.get(student_name)

    # 4. Check if the student was found and display the appropriate message.
    if marks is not None:
        print(f"{student_name}'s marks: {marks}")
    else:
        print("Student not found.")

# Main execution block
if __name__ == "__main__":
    find_student_marks()
