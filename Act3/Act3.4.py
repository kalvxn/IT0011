def read_student_info(file_name):
    with open(file_name, 'r') as file:
        contents = file.readlines()
        for line in contents:
            print(line.strip())

print("Reading Student Information:")
read_student_info("students.txt")
