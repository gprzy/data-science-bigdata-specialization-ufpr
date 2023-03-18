from math import pi


def circumference_metrics(radius):
    perimeter = 2*pi*radius
    area = pi * pow(radius, 2)
    return perimeter, area


def input_circumference_metrics(*args, **kwargs):
    def wrapper(*args, **kwargs):
        radius = float(input('What is the circumference radius (cm)? = '))
        perimeter, area = circumference_metrics(radius)
        
        print(f'\nPerimeter = {round(perimeter, 3)} cm')
        print(f'Area = {round(area, 3)} cm²')
        
    return wrapper


@input_circumference_metrics
def get_circumference_metrics():
    return


if __name__ == '__main__':
    get_circumference_metrics()
