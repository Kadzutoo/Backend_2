# Создание класса Person с атрибутами full_name, age, is_married
class Person:
    def __init__(self, full_name, age, is_married):
        self.full_name = full_name
        self.age = age
        self.is_married = is_married

    #Метод introduce_myself для вывода информации о человеке
    def introduce_myself(self):
        marital_status = "женат/замужем" if self.is_married else "не женат/не замужем"
        print(f"Имя: {self.full_name}, Возраст: {self.age}, Семейное положение: {marital_status}")

# Создание класса Student, наследуемого от Person, с атрибутом marks
class Student(Person):
    def __init__(self, full_name, age, is_married, marks):
        super().__init__(full_name, age, is_married)
        self.marks = marks  # marks — словарь, где ключ — предмет, а значение — оценка

    # Метод для подсчета средней оценки ученика
    def calculate_average_mark(self):
        if self.marks:
            average = sum(self.marks.values()) / len(self.marks)
            return average
        return 0  # если нет оценок, возвращаем 0

    # Переопределение метода introduce_myself для вывода оценок
    def introduce_myself(self):
        super().introduce_myself()
        for subject, mark in self.marks.items():
            print(f"Предмет: {subject}, Оценка: {mark}")
        print(f"Средняя оценка: {self.calculate_average_mark():.2f}")

# Создание класса Teacher, наследуемого от Person
class Teacher(Person):
    base_salary = 30000 # Базовая зарплата как атрибут класса

    def __init__(self, full_name, age, is_married, experience):
        super().__init__(full_name, age, is_married)
        self.experience = experience

    # Метод для расчета зарплаты учителя
    def calculate_salary(self):
        bonus_years = max(0, self.experience - 3)  # бонус начисляется только за годы свыше 3
        bonus = Teacher.base_salary * 0.05 * bonus_years
        return Teacher.base_salary + bonus

    # Метод introduce_myself для вывода информации о зарплате
    def introduce_myself(self):
        super().introduce_myself()
        print(f"Опыт: {self.experience} лет, Зарплата: {self.calculate_salary():.2f} сом.")


# Создание объекта учителя, вывод информации и расчет зарплаты
teacher = Teacher("Сергей Васильев", 40, True, 10)
teacher.introduce_myself()


#Функция для создания списка студентов
def create_students():
    student1 = Student("Халматов Арген", 19, False, {"Математика": 5, "Физика": 5, "Химия": 5})
    student2 = Student("Екубов Шамшод", 20, False, {"Математика": 5, "Физика": 4, "Химия": 4})
    student3 = Student("Сапаров Элдин", 17, False, {"Математика": 3, "Физика": 3, "Химия": 4})
    return [student1, student2, student3]

#Вызов функции create_students и вывод информации по каждому ученику
students = create_students()
for student in students:
    student.introduce_myself()
    print("-" * 30)  # разделитель для удобства чтения

