from math import sqrt


def bhaskara(a, b, c):
    assert a > 0, 'The provided equation is not quadratic!'

    delta = b**2 - 4*a*c
    assert delta >= 0, 'The provided equation dont have real solutions!'

    x1 = -b + sqrt(delta) / 2*a
    x2 = -b - sqrt(delta) / 2*a

    return x1, x2


def input_bhaskara(*args, **kwargs):
    def wrapper(*args, **kwargs):
        a = float(input('Digit a = '))
        b = float(input('Digit b = '))
        c = float(input('Digit c = '))

        roots = bhaskara(a, b, c)

        print(f'\nRoot 1 = {round(roots[0], 3)}')
        print(f'Root 2 = {round(roots[1], 3)}')

    return wrapper


@input_bhaskara
def get_bhaskara():
    return


if __name__ == '__main__':
    get_bhaskara()
