#!/usr/bin/python3
class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        student_dict = {}
        for key, value in self.__dict__.items():
            if isinstance(value, (list, dict, str, int, bool)):
                student_dict[key] = value
        return student_dict

# Example usage:
if __name__ == "__main__":
    student = Student("John", "Doe", 20)
    student_dict = student.to_json()
    print(student_dict)
