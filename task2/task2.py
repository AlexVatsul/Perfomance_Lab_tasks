circle = {}
dots = []

with open('circle.txt', 'r') as file:
    x_str, y_str = file.readline().split()
    r_str = file.readline()

    circle['x'] = float(x_str)
    circle['y'] = float(y_str)
    circle['r'] = float(r_str)

with open('dot.txt', 'r') as file:
    for line in file:
        x_str, y_str = line.split()
        dot = {
            'x': float(x_str),
            'y': float(y_str)
        }
        dots.append(dot)


def formula(a, b):
    r_c = a['r']
    x_c = a['x']
    y_c = a['y']

    for i in b:
        x_d = i['x']
        y_d = i['y']
        r_new = (x_d - x_c)**2 + (y_d - y_c)**2
        if r_new < r_c:
            print(1)
        elif r_new > r_c**2:
            print(2)
        else:
            print(0)

formula(circle, dots)