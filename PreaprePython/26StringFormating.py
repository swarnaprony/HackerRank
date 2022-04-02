def print_formatted(number):
    # your code goes here
    for i in range(1, number+1):
        decimal = i
        octal = format(i,'o')
        hexadecimal= format(i,'X')
        binary = format(i,'b')
        print(f"{(len(str(format(number, 'b')))-len(str(decimal)))*' '}{decimal} {(len(str(format(number, 'b')))-len(str(octal)))*' '}{octal} {(len(str(format(number, 'b')))-len(str(hexadecimal)))*' '}{hexadecimal} {(len(str(format(number, 'b')))-len(str(binary)))*' '}{binary}")

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)