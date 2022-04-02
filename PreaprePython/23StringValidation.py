def string_validation(string):
    print_alnum = 'False'
    print_alpha = 'False'
    print_digit = 'False'
    print_lower = 'False'
    print_upper = 'False'
    for s in string:
        if s.isalnum() == True:
            print_alnum = 'True'
        if s.isalpha() == True:
            print_alpha = 'True'
        if s.isdigit() == True:
            print_digit = 'True'
        if s.islower() == True:
            print_lower = 'True'
        if s.isupper() == True:
            print_upper = 'True'
    return print(f"{print_alnum}\n{print_alpha}\n{print_digit}\n{print_lower}\n{print_upper}")

if __name__ == '__main__':
    s = input()
    validation = string_validation(s)