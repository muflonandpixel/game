import random

def guess_number():
    # Генерируем случайное число от 1 до 100
    secret_number = random.randint(1, 100)
    attempts = 0
    
    print("Привет! Я загадал число от 1 до 100. Попробуй угадать его!")

    while True:
        try:
            guess = int(input("Введи свою догадку: "))
            attempts += 1
            if guess < secret_number:
                print("Мое число больше.")
            elif guess > secret_number:
                print("Мое число меньше.")
            else:
                print("Поздравляю! Ты угадал число {} за {} попыток.".format(secret_number, attempts))
                break
        except ValueError:
            print("Неправильный формат ввода. Попробуй еще раз.")

if __name__ == "__main__":
    guess_number()