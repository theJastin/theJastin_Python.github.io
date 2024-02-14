import random

# Step1 - list of student names
# student_accounts = [
#     {
#         "name" : "ROSSIE MARTINEZ",
#         "id" : "100000",
#         "email" : "RMARTINEZ@adadevelopersacademy.org"
#     },
#     {
#         "name" : "JOHN SMITH",
#         "id" : "100001",
#         "email": "JSMITH@adadevelopersacademy.org"
#     },
#     {
#         "name" : "ANNA BOLD",
#         "id" : "100002",
#         "email" : "ABOLD@adadevelopersacademy.org"
#     },
#     {
#         "name": "JULIA RANCH",
#         "id" : "100003",
#         "email" : "JRANCH@adadevelopersacademy.org"
#     },
#     {
#         "name" : "DELIA AGHO",
#         "id" : "100004",
#         "email" : "DAGHO@adadevelopersacademy.org"
#     }
# ]
student_names = ["ROSSIE MARTINEZ", "JOHN SMITH", "ANNA BOLD", "JULIA RANCH", "DELIA AGHO"]

student_accounts = []
# Step2 - list of student IDs
# Step3 - list of emails (student names, IDs)
for i in range(5):
    student = {}
    student["name"] = student_names[i]
    student["id"] = random.randint(111111, 999999)

    [first, last] = student_names[i].split(" ")
    student["email"] = first[0] + last + str(student["id"])[-3:] + "@example.org"

    print(f'name: {student["name"]}\nid: {student["id"]}\nemail: {student["email"]}\n')

    student_accounts.append(student)

# Print each student account information
# for account in student_accounts:
#     for key in account:
#         print(f'{key}: {account[key]}')
#     print()

# for account in student_accounts:
#     print(f'name: {account.get("name")}\nid:{account.get("id")}\nemail: {account.get("email")}\n')
