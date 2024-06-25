from random import randint

import logger

logger = logger.get_logger(__name__, 'randomizer.log')


def get_input():
    try:
        print("Введите границы интервала от 0 до 100")
        a = int(input("a = "))
        b = int(input("b = "))
        logger.info(f"Введены границы интервала ({a}, {b})")
        return a, b
    except ValueError:
        logger.error('Ошибка ввода')
        return None


def randomizer(a, b):
    if not (0 < a <= 100) or not (0 < b <= 100):
        raise ValueError
    return randint(a, b)


def main():

    input_data = get_input()
    if input_data:
        try:
            return randomizer(*input_data)
        except ValueError:
            logger.error("Введены неверные границы интервала")


if __name__ == '__main__':
    logger.info("Старт программы")
    result = None
    while not result:
        result = main()
    else:
        print(f"Результат: {result}")
        logger.info("Работа завершена")
