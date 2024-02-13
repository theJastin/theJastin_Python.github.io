import random

# Step1 - list of student names
student_names = ["ROSSIE MARTINEZ", "JOHN SMITH", "ANNA BOLD", "JULIA RANCH", "DELIA AGHO"]

# Step2 - list of student IDs
student_ids = []
for i in range(5): # for name in student_names
    student_ids.append(random.randint(111111, 999999))

# Step3 - list of emails (student names, IDs)
student_emails = []
for i in range(5):
    student_name = student_names[i]
    [first, last] = student_name.split(" ")

    student_id = str(student_ids[i])
    student_emails.append(first[0] + last + str(student_id[-3:]) + "@example.org")

# Print each student account information
for i in range(5):
    print(f"name: {student_names[i]}\nid: {student_ids[i]}\nemail: {student_emails[i]}\n")
