import random


def play_game(min_value, max_value, attempts, initial_capital):
    print(f"Добро пожаловать в игру 'Угадай число'!")
    print(f"У вас {initial_capital} монет. Попробуйте угадать число от {min_value} до {max_value}.")
    print(f"У вас {attempts} попыток.\n")

    target_number = random.randint(min_value, max_value)
    capital = initial_capital

    for attempt in range(1, attempts + 1):
        print(f"Попытка {attempt} из {attempts}")
        print(f"Ваш текущий капитал: {capital}")

        while True:
            try:
                bet = int(input("Введите сумму ставки: "))
                if bet > capital:
                    print("Ставка превышает ваш текущий капитал. Попробуйте снова.")
                elif bet <= 0:
                    print("Ставка должна быть больше 0. Попробуйте снова.")
                else:
                    break
            except ValueError:
                print("Некорректный ввод. Введите число.")

        while True:
            try:
                guess = int(input(f"Введите число от {min_value} до {max_value}: "))
                if guess < min_value or guess > max_value:
                    print(f"Число должно быть в диапазоне от {min_value} до {max_value}. Попробуйте снова.")
                else:
                    break
            except ValueError:
                print("Некорректный ввод. Введите число.")

        if guess == target_number:
            print("Поздравляем! Вы угадали число!")
            capital += bet * 2
            print(f"Ваш капитал удвоился и теперь составляет: {capital}")
            break
        else:
            print("Неправильно! Вы потеряли свою ставку.")
            capital -= bet
            if capital <= 0:
                print("Вы проиграли весь капитал!")
                return False

    if capital > 0:
        print(f"Игра окончена. Ваш итоговый капитал: {capital}")
        return True
    else:
        print("Игра окончена. Вы проиграли.")
        return False
