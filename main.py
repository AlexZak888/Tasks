class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.average_grade = float()

    def rate_l(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def average_grade(self):
        grades_count = 0
        if not self.grades:
            return 0
        spisok = []
        for k in self.grades:
            grades_count += len(self.grades[k])
            spisok.extent(k)
        return float(sum(spisok) / max(len(spisok), 1))

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания:\
        {self.average_grade}\nКурсы в процессе изучения: {self.courses_in_progress}\nЗавершенные курсы:\
        {self.finished_courses}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Такое сравнение некорректно')
            return
        return self.average_grade < other.average_grade


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        self.average_grade = float()

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average_grade}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Такое сравнение некорректно')
            return
        return self.average_grade < other.average_grade

    def average_grade(self):
        grades_count = 0
        if not self.grades:
            return 0
        spisok = []
        for k in self.grades.values():
            grades_count += len(self.grades[k])
            spisok.extent(k)
        return float(sum(spisok) / max(len(spisok), 1))


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}'
        return res


best_student = Student('Michal', 'Tramp', 'M')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['Git']
best_student.finished_courses += ['Введение в программирование']
best_student2 = Student('Eva', 'Midl', 'W')
best_student2.courses_in_progress += ['Python']
best_student2.courses_in_progress += ['Git']
best_student2.finished_courses += ['Введение в программирование']

cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python']
cool_reviewer2 = Reviewer('Wild', 'West')
cool_reviewer2.courses_attached += ['Git']

cool_lecturer = Lecturer('Evan', 'Lucky')
cool_lecturer.courses_attached += ['Python']
cool_lecturer2 = Lecturer('Vin', 'Diz')
cool_lecturer2.courses_attached += ['Git']

cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student2, 'Python', 9)
cool_reviewer2.rate_hw(best_student, 'Git', 9)
cool_reviewer2.rate_hw(best_student2, 'Git', 10)

best_student.rate_l(cool_lecturer, 'Python', 10)
best_student.rate_l(cool_lecturer2, 'Git', 9)
best_student2.rate_l(cool_lecturer, 'Python', 10)
best_student2.rate_l(cool_lecturer2, 'Git', 9)

student_list = [best_student, best_student2]
lecturer_list = [cool_lecturer, cool_lecturer2]


def student_rating(student_list, course_name):
    sum_all = 0
    count_all = []
    for stud in student_list:
        if stud.courses_in_progress == [course_name]:
            sum_all += len(student_list[stud])
            count_all.extent(stud)
    return float(sum(sum_all)/max(len(count_all), 1))


def lecturer_rating(lecturer_list, course_name):
    sum_all = 0
    count_all = 0
    for lect in lecturer_list:
        if lect.courses_attached == [course_name]:
            sum_all += len(lecturer_list[lect])
            count_all.extent(lect)
    return float(sum(sum_all) / max(len(count_all), 1))