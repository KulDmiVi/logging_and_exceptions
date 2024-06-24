def get_input_data():
    string_list = input('Введите числа через запятую: ').split(',')
    try:
        numbers = tuple(map(float, string_list))
        return numbers
    except ValueError:
        print("Ошибка ввода данных")


def arithmetic_mean(numbers):
    average = sum(numbers) / len(numbers)
    return average


def main():
    numbers = get_input_data()
    if numbers:
        return arithmetic_mean(numbers)


if __name__ == '__main__':
    result = None
    while not result:
        result = main()
    else:
        print(f"Cреднее арифметическое чисел: {result}")
