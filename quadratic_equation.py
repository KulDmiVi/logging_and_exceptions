import math

import logger

loger = logger.get_logger(__name__, 'quadratic.log')


def input_data():
    try:
        a = float(input("a = "))
        if a == 0.0:
            raise ValueError
        b = float(input("b = "))
        c = float(input("c = "))
        loger.info(f'Введены коэффициенты уравнения: {a}, {b}, {c}')
        return a, b, c
    except ValueError:
        loger.error("Введен неверный коэффициент")
        return None


def get_discr(a, b, c):
    discr = b ** 2 - 4 * a * c
    loger.info(f'Вычислен дискриминанта: {discr}')
    return discr


def calc_roots_equation(a, b, discr):
    if discr > 0:
        x1 = round((-b + math.sqrt(discr)) / (2 * a), 2)
        x2 = round((-b - math.sqrt(discr)) / (2 * a), 2)
        loger.info(f'Найдено два корня квадратного уравнения: {x1} {x2}')
        return x1, x2
    elif discr == 0:
        x = round(-b / (2 * a), 2)
        loger.info(f'Найден единственный корень квадратного уравнения: {x}')
        return x
    else:
        loger.info('Уравнение не имеет действительных корней')
        return 'Уравнение не имеет действительных корней'


def main():
    print("Введите коэффициенты для уравнения")
    print("ax^2 + bx + c = 0:")
    coefficients = input_data()
    if coefficients:
        koef1, koef2, koef3 = coefficients
        discriminant = get_discr(koef1, koef2, koef3)
        result = calc_roots_equation(koef1, koef2, discriminant)
        return result
    else:
        return None


if __name__ == '__main__':
    loger.info(f'Старт программы')
    result = None
    while not result:
        result = main()
    else:
        print(f'Результат: {result}')
        loger.info('Завершение программы')



