from dataclasses import dataclass


@dataclass()
class Course:
    course_name: str
    classroom: str
    teacher: str
    etcs: int
    grade: None or int


@dataclass()
class DataSheet:
    course: list[Course]

    def get_grades_as_list(self):
        grades_list = []
        for i in self.course:
            grades_list.append(i.grade)

        return self.course


class Student:
    name: str
    gender: int
    data_sheet: DataSheet
    img_url = str

    def __init__(self, name: str, gender: int, data_sheet: DataSheet, img_url: str):
        self.name = name
        self.gender = gender
        self.data_sheet = data_sheet
        self.img_url = img_url

    def get_avg_grade(self):
        sum_num = 0
        grade_list = self.data_sheet.get_grades_as_list()
        for g in grade_list:
            sum_num = sum_num + g.grade

        avg = sum_num / len(grade_list)
        return avg


def gen_students(n: int):
    pass


if __name__ == "__main__":
    course_1 = Course("Math", "C105", "Bent", 80, 7)
    course_2 = Course("Computer Science", "C207", "Henrik", 50, 12)
    course_3 = Course("Danish", "C257", "Anette", 20, 2)

    course_list = [course_1, course_2]
    course_list_2 = [course_1, course_2, course_3]

    the_data_sheet = DataSheet(course_list)
    the_data_sheet_2 = DataSheet(course_list_2)

    frederik = Student("Frederik", 1, the_data_sheet, "image")
    casperine = Student("Casper", 0, the_data_sheet_2, "image")

    student_list = [frederik, casperine]

    for student in student_list:
        print(f"{student.name} {student.gender} {student.data_sheet.get_grades_as_list()}")
        print(f"{student.name} grade avg: {student.get_avg_grade()}")
