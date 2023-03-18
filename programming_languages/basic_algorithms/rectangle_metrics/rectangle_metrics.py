from math import sqrt


def rectangle_metrics(a, b):
    area = a*b
    diagonal = sqrt(a**2 + b**2)
    return area, diagonal


def input_rectangle_side(*args, **kwargs):
    def wrapper(*args, **kwargs):
        a = float(input('What is the side a of the rectangle (cm)? = '))
        b = float(input('What is the side b of the rectangle? (cm) = '))
        area, diagonal = rectangle_metrics(a, b)
        
        print(f'\nArea = {round(area, 3)} cm²')
        print(f'Diagonal = {round(diagonal, 3)} cm')
        
    return wrapper


@input_rectangle_side
def get_rectangle_metrics():
    return


if __name__ == '__main__':
    get_rectangle_metrics()
