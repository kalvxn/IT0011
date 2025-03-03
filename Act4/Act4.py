import pickle

class StudentRecord:
    def __init__(self, student_id, full_name, class_standing, major_exam_grade):
        self.student_id = student_id
        self.full_name = full_name
        self.class_standing = class_standing
        self.major_exam_grade = major_exam_grade

    def calculate_grade(self):
        return (self.class_standing * 0.6) + (self.major_exam_grade * 0.4)

class RecordManagement:
    def __init__(self):
        self.records = []

    def open_file(self, filename):
        with open(filename, 'rb') as file:
            self.records = pickle.load(file)

    def save_file(self, filename):
        with open(filename, 'wb') as file:
            pickle.dump(self.records, file)

    def show_all_records(self):
        for record in self.records:
            print(f"ID: {record.student_id}, Name: {record.full_name}, Class Standing: {record.class_standing}, Major Exam Grade: {record.major_exam_grade}, Final Grade: {record.calculate_grade()}")

    def order_by_last_name(self):
        self.records.sort(key=lambda x: x.full_name[1])

    def order_by_grade(self):
        self.records.sort(key=lambda x: x.calculate_grade(), reverse=True)

    def show_student_record(self, student_id):
        for record in self.records:
            if record.student_id == student_id:
                print(f"ID: {record.student_id}, Name: {record.full_name}, Class Standing: {record.class_standing}, Major Exam Grade: {record.major_exam_grade}, Final Grade: {record.calculate_grade()}")
                return
        print("Record not found.")

    def add_record(self, student_id, full_name, class_standing, major_exam_grade):
        new_record = StudentRecord(student_id, full_name, class_standing, major_exam_grade)
        self.records.append(new_record)

    def edit_record(self, student_id, class_standing=None, major_exam_grade=None):
        for record in self.records:
            if record.student_id == student_id:
                if class_standing is not None:
                    record.class_standing = class_standing
                if major_exam_grade is not None:
                    record.major_exam_grade = major_exam_grade
                return
        print("Record not found.")

    def delete_record(self, student_id):
        for record in self.records:
            if record.student_id == student_id:
                self.records.remove(record)
                return
        print("Record not found.")

def main():
    manager = RecordManagement()
    while True:
        print("\nMenu:")
        print("1. Open File")
        print("2. Save File")
        print("3. Show All Students Record")
        print("4. Order by Last Name")
        print("5. Order by Grade")
        print("6. Show Student Record")
        print("7. Add Record")
        print("8. Edit Record")
        print("9. Delete Record")
        print("0. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            filename = input("Enter filename to open: ")
            manager.open_file(filename)
        elif choice == '2':
            filename = input("Enter filename to save: ")
            manager.save_file(filename)
        elif choice == '3':
            manager.show_all_records()
        elif choice == '4':
            manager.order_by_last_name()
        elif choice == '5':
            manager.order_by_grade()
        elif choice == '6':
            student_id = input("Enter Student ID: ")
            manager.show_student_record(student_id)
        elif choice == '7':
            student_id = input("Enter Student ID: ")
            full_name = (input("Enter First Name: "), input("Enter Last Name: "))
            class_standing = float(input("Enter Class Standing: "))
            major_exam_grade = float(input("Enter Major Exam Grade: "))
            manager.add_record(student_id, full_name, class_standing, major_exam_grade)
        elif choice == '8':
            student_id = input("Enter Student ID: ")
            class_standing = input("Enter new Class Standing (leave blank to skip): ")
            major_exam_grade = input("Enter new Major Exam Grade (leave blank to skip): ")
            manager.edit_record(student_id, float(class_standing) if class_standing else None, float(major_exam_grade) if major_exam_grade else None)
        elif choice == '9':
            student_id = input("Enter Student ID to delete: ")
            manager.delete_record(student_id)
        elif choice == '0':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()