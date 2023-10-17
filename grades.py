# A dictionary to map subject numbers to subject names
subject_names = {}
for i in range(1, 5):
    subject_name = input(f"Enter the name of subject {i}: ")
    subject_names[i] = subject_name

# an empty dictionary to store student data
student_data = {}

student_number = int(input("Enter the student number: "))

marks = []
for subject_number in range(1, 5):
    while True:
        try:
            mark = float(input(f"Enter the mark for {subject_names[subject_number]}: "))
            if 0 <= mark <= 100:
                marks.append(mark)
                break
            else:
                print("Error: Mark should be between 0 and 100.")
        except ValueError:
            print("Invalid number")

# Calculate the average mark
average_mark = sum(marks) / len(marks)

#Compute grade from average
if average_mark >=0 and average_mark<= 30:
    grade="D"
elif average_mark >=31 and average_mark<=50:
    grade="C"
elif average_mark >=51 and average_mark<=70:
    grade="B"
elif average_mark>71 and average_mark<=100:
    grade="A"

# Store the student data in the dictionary
student_data['Student Number'] = student_number
student_data['Subject Marks'] = marks
student_data['Average Mark'] = average_mark
student_data['Grade'] = grade

# Print the student data with subject names
print("\nStudent Data:")
for key, value in student_data.items():
    if key == 'Subject Marks':
        subject_marks = [f"{subject_names[i]}: {mark}" for i, mark in enumerate(value, start=1)]
        print('\n'.join(subject_marks))
    else:
        print(f"{key}: {value}")
