from random import randint


def get_input():
    try:
        a = int(input("a = "))
        b = int(input("b = "))
        return a, b
    except ValueError:
        print('Ошибка ввода. Введите два целых числа от 0 до 100')
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
            print('Ошибка ввода диапазона')


if __name__ == '__main__':
    result = None
    while not result:
        result = main()
    else:
        print(result)
