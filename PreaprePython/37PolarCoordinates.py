import string
import cmath

def polarCoordinates(real_part, imaginary_part):
    absolute_value = abs(complex(real_part, imaginary_part))
    print(absolute_value)
    argument = cmath.phase(complex(real_part, imaginary_part))
    print(argument)
    return

if __name__ == '__main__':
    complex_number = input()
    if '+' in complex_number[1:]:
        complex_number = complex_number.split('+')
        real_part = int(complex_number[0])
        imaginary_part = int(complex_number[1].replace('j', ''))
    elif '-' in complex_number[1:]:
        complex_number = complex_number.split('-')
        real_part = int(complex_number[0])
        imaginary_part = int('-' + complex_number[1].replace('j', ''))

    polarCoordinates(real_part, imaginary_part)