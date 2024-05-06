import random

def guess_number(max_attempts, min_range, max_range):
    secret_number = random.randint(min_range, max_range)
    attempts = 0

    print("Привет! Я загадал число от {} до {}. Попробуй угадать его за {} попыток.".format(min_range, max_range, max_attempts))

    while attempts < max_attempts:
        try:
            guess = int(input("Введи свою догадку: "))
            attempts += 1

            if guess < secret_number:
                print("Мое число больше.")
            elif guess > secret_number:
                print("Мое число меньше.")
            else:
                print("Поздравляю! Ты угадал число {} за {} попыток.".format(secret_number, attempts))
                return True
        except ValueError:
            print("Неправильный формат ввода. Попробуй еще раз.")

    print("К сожалению, ты исчерпал все попытки. Загаданное число было {}.".format(secret_number))
    return False

def main():
    max_attempts = 5
    min_range = 1
    max_range = 100

    games_played = 0
    games_won = 0

    while True:
        if guess_number(max_attempts, min_range, max_range):
            games_won += 1
        games_played += 1

        play_again = input("Хочешь сыграть еще раз? (да/нет): ")
        if play_again.lower() != "да":
            print("Спасибо за игру! Сыграно {} игр, выиграно {}.".format(games_played, games_won))
            break

if __name__ == "__main__":
    main()