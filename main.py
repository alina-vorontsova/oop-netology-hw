students_list = []
lecturers_list = []

class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        students_list.append(self)

    def rate_lecture(self, lecturer, course, grade): 
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached and 0 <= grade < 11:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'   

    def _average(self):
        counter = 0
        for value in self.grades.values():
            for v in value:
                counter += 1
        average_grade = sum(map(sum, self.grades.values())) / counter
        return average_grade

    def _progress(self):
        courses_in_progress = ', '.join(self.courses_in_progress)
        return courses_in_progress

    def _finished(self):
        finished_courses = ', '.join(self.finished_courses)
        return finished_courses

    def __str__(self):
        info_ = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self._average()}\nКурсы в процессе изучения: {self._progress()}\nЗавершенные курсы: {self._finished()}'
        return info_

    def __lt__(self, other):
        res = self._average() < other._average()
        return res

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
  
    def __str__(self):
        info_ = f'Имя: {self.name}\nФамилия: {self.surname}'
        return info_
 
class Lecturer (Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []
        self.grades = {}
        lecturers_list.append(self)

    def _average(self):
        counter = 0
        for value in self.grades.values():
            for v in value:
                counter += 1
        average_grade = sum(map(sum, self.grades.values())) / counter
        return average_grade

    def __str__(self):
        info_ = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self._average()}'
        return info_

    def __lt__(self, other):
        res = self._average() < other._average()
        return res

class Reviewer (Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress and 0 <= grade < 11:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        info_ = f'Имя: {self.name}\nФамилия: {self.surname}'
        return info_

def course_grade_average(group, course): # group = students_list OR lecturers_list; course = 'Python' OR 'Java' OR 'C++'
    sum_grades = 0 
    grades_num = 0
    for person in group:
        for k, value in person.grades.items():
            if course in k:
                for v in value:
                    sum_grades += v
                    grades_num += 1
    average_grade_for_course = sum_grades / grades_num
    return average_grade_for_course

student1 = Student('Иван', 'Иванов', 'мужской')
student1.courses_in_progress += ['Python', 'C++']
student1.finished_courses += ['Java']

student2 = Student('Елена', 'Еленовна', 'женский')
student2.courses_in_progress += ['Java', 'Python']
student2.finished_courses += ['С++']

mentor1 = Mentor('Герасим', 'Грустный')
mentor1.courses_attached += ['Python', 'Java']

mentor2 = Mentor('Степан', 'Веселый')
mentor2.courses_attached += ['Java', 'C++']

lecturer1 = Lecturer('Додик', 'Сибирский')
lecturer1.courses_attached += ['Python', 'C++']

lecturer2 = Lecturer('Кирилл', 'Ладожский')
lecturer2.courses_attached += ['Java', 'Python']

reviewer1 = Reviewer('Лев', 'Степной')
reviewer1.courses_attached += ['Python', 'C++']

reviewer2 = Reviewer('Волк', 'Цирковой')
reviewer2.courses_attached += ['Java', 'C++']

student1.rate_lecture(lecturer1, 'Python', 10)
student1.rate_lecture(lecturer1, 'Python', 2)
student1.rate_lecture(lecturer1, 'C++', 7)
student1.rate_lecture(lecturer1, 'C++', 9)

student2.rate_lecture(lecturer2, 'Java', 5)
student2.rate_lecture(lecturer2, 'C++', 10)
student2.rate_lecture(lecturer2, 'Python', 10)
student2.rate_lecture(lecturer2, 'Python', 2)

reviewer1.rate_hw(student1, 'Python', 10)
reviewer1.rate_hw(student1, 'Python', 5)
reviewer2.rate_hw(student1, 'C++', 10)
reviewer2.rate_hw(student1, 'C++', 5)

reviewer2.rate_hw(student2, 'Java', 3)
reviewer2.rate_hw(student2, 'Java', 9)
reviewer1.rate_hw(student2, 'Python', 2)
reviewer1.rate_hw(student2, 'Python', 7)