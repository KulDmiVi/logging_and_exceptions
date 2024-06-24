import math


def input_data():
    try:
        a = float(input("a = "))
        b = float(input("b = "))
        c = float(input("c = "))
        return a, b, c
    except ValueError:
        print("Ошибка ввода! Коэффициенты a, b, c - числа")
        return None


def get_discr(a, b, c):
    discr = b ** 2 - 4 * a * c
    return discr


def calc_roots_equation(a, b, discr):
    if discr > 0:
        try:
            x1 = round((-b + math.sqrt(discr)) / (2 * a), 2)
            x2 = round((-b - math.sqrt(discr)) / (2 * a), 2)
            return x1, x2
        except ZeroDivisionError:
            return "Коэффициент 'а' должен быть равен = 0 "

    elif discr == 0:
        try:
            x = round(-b / (2 * a), 2)
            return x
        except ZeroDivisionError:
            return "Коэффициент 'а' должен быть равен = 0 "

    else:
        return 'Уравнение не имеет действительных корней'


if __name__ == '__main__':
    print("Введите коэффициенты для уравнения")
    print("ax^2 + bx + c = 0:")
    coefficients = input_data()
    if coefficients:
        koef1, koef2, koef3 = coefficients
        discriminant = get_discr(koef1, koef2, koef3)
        result = calc_roots_equation(koef1, koef2, discriminant)
        print(result)


