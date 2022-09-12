import random
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
    courses: list[Course]

    def get_grades_as_list(self):
        grades_list = []
        for i in self.courses:
            grades_list.append(i.grade)

        return self.courses


class Student:
    name: str
    gender: int
    data_sheet: DataSheet
    img_url = str

    def __init__(self, name: str, gender: int, data_sheet: DataSheet or None, img_url: str):
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


@dataclass()
class Simple_Student:
    name: str
    age: int
    gender: int


def gen_students(n: int):
    names = []
    returnable_students = []
    with open("../data/names.txt", "r") as names_file:
        for name in names_file:
            names.append(name)
    _course_1 = Course("Math", "C105", "Bent", 80, 7)
    _course_2 = Course("Computer Science", "C207", "Henrik", 50, 12)
    _course_3 = Course("Danish", "C257", "Anette", 20, 2)
    courses = [_course_1, _course_2, _course_3]
    img_link_template = "https://www.fakelink.com/img"

    # Random Courses
    for i in range(n):
        random_courses = []
        for course in courses:
            if random.randint(0, 1) > 0.5:
                random_courses.append(course)

        random_name = names[random.randint(0, len(names))]
        random_gender = random.randint(0, 1)

        _datasheet = DataSheet(random_courses)
        generated_student = Student(random_name, random_gender, _datasheet,
                                    f"{img_link_template}/{random.randrange(1, 1000)}")
        returnable_students.append(generated_student)

    for i in returnable_students:
        print(f"{i.gender} {i.name} {i.img_url} {len(returnable_students)}")

    # Write generated students to file
    with open("../data/generate_students.csv", "w") as generated_student_file:
        buffer = "Name;Gender;Courses;imageUrl \n"
        for i in returnable_students:
            course_buffer = ""
            if i.data_sheet.courses is None:
                continue
            for j in i.data_sheet.courses:
                course_buffer += f"{j} "
            buffer += f"{i.name};{i.gender};{course_buffer};{i.img_url} \n"

        generated_student_file.write(buffer)

    return returnable_students


def read_students_into_list(file: str):
    list_of_students = []
    with open(file, "r") as student_file:
        print("\n\n **READ GENERATED STUDENTS FROM FILE** \n\n")
        for line in student_file:
            name, gender, data_sheet, image_url = line.split(";")
            read_student = Student(name, gender, data_sheet, image_url)
            print(f"{read_student.name} {read_student.gender} {read_student.data_sheet} {read_student.img_url}")

    # sorted_list_of_students = list_of_students.sort(key=lambda k: )


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

    gen_students(122)
    for student in student_list:
        print(f"{student.name} {student.gender} {student.data_sheet.get_grades_as_list()}")
        print(f"{student.name} grade avg: {student.get_avg_grade()}")

    read_students_into_list("../data/generate_students.csv")
