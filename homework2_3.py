class Computer:
    def __init__(self, cpu, memory):
        self.__cpu = cpu
        self.__memory = memory

    # Геттеры и сеттеры для атрибутов cpu и memory
    @property
    def cpu(self):
        return self.__cpu

    @cpu.setter
    def cpu(self, value):
        self.__cpu = value

    @property
    def memory(self):
        return self.__memory

    @memory.setter
    def memory(self, value):
        self.__memory = value

    # Метод для выполнения арифметических операций с атрибутами
    def make_computations(self):
        return f"Сложение: {self.__cpu + self.__memory}, Умножение: {self.__cpu * self.__memory}"

    # Переопределение магического метода __str__
    def __str__(self):
        return f"Компьютер с CPU: {self.__cpu} и Memory: {self.__memory}GB"

    # Переопределение всех методов сравнения по атрибуту memory
    def __eq__(self, other):
        return self.__memory == other.memory

    def __ne__(self, other):
        return self.__memory != other.memory

    def __lt__(self, other):
        return self.__memory < other.memory

    def __le__(self, other):
        return self.__memory <= other.memory

    def __gt__(self, other):
        return self.__memory > other.memory

    def __ge__(self, other):
        return self.__memory >= other.memory


class Phone:
    def __init__(self, sim_cards_list):
        self.__sim_cards_list = sim_cards_list

    # Геттер и сеттер для списка сим-карт
    @property
    def sim_cards_list(self):
        return self.__sim_cards_list

    @sim_cards_list.setter
    def sim_cards_list(self, value):
        self.__sim_cards_list = value

    # Метод симуляции звонка
    def call(self, sim_card_number, call_to_number):
        if 1 <= sim_card_number <= len(self.__sim_cards_list):
            sim_card = self.__sim_cards_list[sim_card_number - 1]
            print(f"Идет звонок на номер {call_to_number} с сим-карты-{sim_card_number} - {sim_card}")
        else:
            print("Некорректный номер сим-карты")

    # Переопределение магического метода __str__
    def __str__(self):
        return f"Телефон с SIM-картами: {', '.join(self.__sim_cards_list)}"


class SmartPhone(Computer, Phone):
    def __init__(self, cpu, memory, sim_cards_list):
        Computer.__init__(self, cpu, memory)
        Phone.__init__(self, sim_cards_list)

    # Метод для использования GPS
    def use_gps(self, location):
        print(f"Построение маршрута до {location}")

    # Переопределение магического метода __str__
    def __str__(self):
        return f"Смартфон с CPU: {self.cpu}, Memory: {self.memory}GB и SIM-картами: {', '.join(self.sim_cards_list)}"


# Создание объектов
computer = Computer(cpu=4, memory=16)
phone = Phone(sim_cards_list=["Beeline", "MegaCom"])
smartphone1 = SmartPhone(cpu=8, memory=32, sim_cards_list=["O!", "MegaCom"])
smartphone2 = SmartPhone(cpu=6, memory=64, sim_cards_list=["Beeline", "O!"])

# Печать информации о созданных объектах
print(computer)
print(phone)
print(smartphone1)
print(smartphone2)

# Тестирование методов объектов
# Методы компьютера
print(computer.make_computations())
print(computer == smartphone1)  # Сравнение по памяти
print(computer != smartphone2)
print(computer < smartphone2)

# Методы телефона
phone.call(1, "+996 777 99 88 11")
phone.call(2, "+996 555 66 77 33")

# Методы смартфона
smartphone1.use_gps("г. Бишкек")
smartphone1.make_computations()
smartphone1.call(1, "+996 700 88 99 00")
smartphone2.use_gps("г. Ош")
