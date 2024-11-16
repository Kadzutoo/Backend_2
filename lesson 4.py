import random


# Базовый класс для персонажей
class Character:
    def __init__(self, name, health, mana, attack_power):
        self.name = name
        self.health = health
        self.mana = mana
        self.attack_power = attack_power
        self.is_stunned = False

    def is_alive(self):
        return self.health > 0

    def take_damage(self, damage):
        self.health -= damage
        print(f"{self.name} получает {damage} урона. Здоровье: {self.health}")

    def use_mana(self, amount):
        if self.mana >= amount:
            self.mana -= amount
            return True
        else:
            print(f"{self.name} не хватает маны!")
            return False


# Классы для героев
class Knight(Character):
    def attack(self):
        if not self.is_stunned:
            damage = self.attack_power + random.randint(3, 5)
            print(f"Рыцарь наносит удар мечом, нанося {damage} урона.")
            return damage
        else:
            print(f"{self.name} оглушен и пропускает ход!")
            self.is_stunned = False
            return 0

    def shield_bash(self, target):
        if self.use_mana(10):
            damage = self.attack_power + random.randint(5, 8)
            target.is_stunned = True
            print(f"Рыцарь использует Удар Щитом, нанося {damage} урона и оглушая {target.name}.")
            return damage
        return 0


class Mage(Character):
    def attack(self):
        if not self.is_stunned:
            damage = self.attack_power + random.randint(8, 12)
            print(f"Маг выпускает огненный шар, нанося {damage} урона.")
            return damage
        else:
            print(f"{self.name} оглушен и пропускает ход!")
            self.is_stunned = False
            return 0

    def cast_poison(self, target):
        if self.use_mana(15):
            print(f"Маг накладывает яд на {target.name}. {target.name} будет получать урон каждый ход.")
            target.poisoned = True
            return 0
        return 0


class Tank(Character):
    def attack(self):
        if not self.is_stunned:
            damage = self.attack_power + random.randint(2, 4)
            print(f"Танк атакует с щитом, нанося {damage} урона.")
            return damage
        else:
            print(f"{self.name} оглушен и пропускает ход!")
            self.is_stunned = False
            return 0

    def taunt(self, target):
        if self.use_mana(10):
            print(f"Танк использует Провокацию! Дракон будет атаковать его в следующем ходу.")
            target.forced_target = self
            return 0
        return 0


class Archer(Character):
    def attack(self):
        if not self.is_stunned:
            damage = self.attack_power + random.randint(5, 10)
            print(f"Стрелок выпускает стрелу, нанося {damage} урона.")
            return damage
        else:
            print(f"{self.name} оглушен и пропускает ход!")
            self.is_stunned = False
            return 0

    def critical_shot(self, target):
        if self.use_mana(12):
            damage = self.attack_power * 2 + random.randint(5, 10)
            print(f"Стрелок выпускает критический выстрел, нанося {damage} урона!")
            return damage
        return 0


class Healer(Character):
    def attack(self):
        print("Хиллер не атакует, но может лечить союзников.")
        return 0

    def heal(self, target):
        if self.use_mana(15):
            heal_amount = random.randint(10, 20)
            target.health += heal_amount
            print(
                f"Хиллер восстанавливает {heal_amount} здоровья герою {target.name}. Здоровье {target.name}: {target.health}")
            return 0
        return 0


# Класс для босса
class Dragon(Character):
    def __init__(self, name, health, mana, attack_power):
        super().__init__(name, health, mana, attack_power)
        self.forced_target = None
        self.poisoned = False

    def attack(self):
        if not self.is_stunned:
            damage = self.attack_power + random.randint(5, 15)
            print(f"Дракон атакует, нанося {damage} урона.")
            return damage
        else:
            print(f"{self.name} оглушен и пропускает ход!")
            self.is_stunned = False
            return 0

    def special_attack(self):
        print("Дракон использует Огненное дыхание!")
        return self.attack_power + random.randint(10, 25)

    def take_damage(self, damage):
        super().take_damage(damage)
        if self.poisoned:
            poison_damage = random.randint(3, 6)
            self.health -= poison_damage
            print(f"{self.name} получает {poison_damage} урона от яда. Здоровье: {self.health}")


# Инициализация героев и босса
heroes = [
    Knight("Рыцарь", health=120, mana=30, attack_power=12),
    Mage("Маг", health=80, mana=40, attack_power=10),
    Tank("Танк", health=160, mana=25, attack_power=8),
    Archer("Стрелок", health=90, mana=20, attack_power=10),
    Healer("Хиллер", health=70, mana=50, attack_power=0)
]

dragon = Dragon("Дракон", health=350, mana=0, attack_power=20)

# Основной цикл игры
turn = 1
while dragon.is_alive() and any(hero.is_alive() for hero in heroes):
    print(f"\n--- Ход {turn} ---")

    # Ход героев
    for hero in heroes:
        if hero.is_alive():
            action = hero.attack()
            dragon.take_damage(action)
            if not dragon.is_alive():
                print("Герои победили дракона!")
                break
            # Специальные действия
            if isinstance(hero, Knight):
                if random.choice([True, False]):
                    action = hero.shield_bash(dragon)
                    dragon.take_damage(action)
            elif isinstance(hero, Mage):
                if random.choice([True, False]):
                    hero.cast_poison(dragon)
            elif isinstance(hero, Tank):
                if random.choice([True, False]):
                    hero.taunt(dragon)
            elif isinstance(hero, Archer):
                if random.choice([True, False]):
                    action = hero.critical_shot(dragon)
                    dragon.take_damage(action)
            elif isinstance(hero, Healer):
                ally = random.choice([h for h in heroes if h.is_alive() and h.health < 100])
                hero.heal(ally)

            input("\nНажмите Enter, чтобы продолжить к следующему герою...")

    if not dragon.is_alive():
        break

    # Ход дракона
    print("\nХод Дракона:")
    if turn % 3 == 0:  # Каждые три хода дракон делает специальную атаку
        damage = dragon.special_attack()
    else:
        damage = dragon.attack()

    if dragon.forced_target and dragon.forced_target.is_alive():
        target = dragon.forced_target
    else:
        target = random.choice([hero for hero in heroes if hero.is_alive()])

    target.take_damage(damage)

    # Проверка, живы ли герои
    if not any(hero.is_alive() for hero in heroes):
        print("Дракон победил героев!")
        break

    turn += 1
    input("\nНажмите Enter, чтобы перейти к следующему ходу...")

# Результат игры
if dragon.is_alive():
    print("\nДракон побеждает! Конец игры.")
else:
    print("\nГерои победили! Конец игры.")
