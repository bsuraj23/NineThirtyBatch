V# Dictionary to store student data
students = {
    "101": {"name": "Alice", "marks": {"Math": 85, "Science": 92, "English": 88}},
    "102": {"name": "Bob", "marks": {"Math": 75, "Science": 64, "English": 80}},
    "103": {"name": "Charlie", "marks": {"Math": 95, "Science": 89, "English": 93}},
}

# Function to calculate average
def calculate_average(marks):
    return sum(marks.values()) / len(marks)

# Print all student details with average
for roll, details in students.items():
    avg = calculate_average(details["marks"])
    print(f"Roll No: {roll}, Name: {details['name']}, Average Marks: {avg:.2f}")