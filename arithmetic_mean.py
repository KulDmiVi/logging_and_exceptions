import logger

logger = logger.get_logger(__name__, 'arithmetic_mean.log')


def get_input_data():
    string_list = input('Введите числа через запятую: ').split(',')
    try:
        numbers = tuple(map(float, string_list))
        logger.info(f"Введена последовательность {numbers}")
        return numbers
    except ValueError:
        logger.error("Ошибка ввода данных")


def arithmetic_mean(numbers):
    average = sum(numbers) / len(numbers)
    logger.info(f"Вычислено среднее арифметическое")
    return average


def main():
    numbers = get_input_data()
    if numbers:
        return arithmetic_mean(numbers)


if __name__ == '__main__':
    logger.info("Старт программы")
    result = None
    while not result:
        result = main()
    else:
        print(f"Cреднее арифметическое чисел: {result}")
        logger.info("Работа завершена")
