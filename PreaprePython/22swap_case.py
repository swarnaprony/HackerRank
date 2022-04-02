def swap_case(s):
    swap_string = ''
    for i in s:
        if i.isupper() == True:
          swap_string = swap_string + i.lower()
        elif i.isupper() == False:
            swap_string = swap_string + i.upper()
        else:
            swap_string = swap_string + i
    return swap_string

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)