import textwrap

def wrap(string, max_width):
    new_string = ''
    for i in range(0,len(string)):
        if i==0:
            new_string = new_string + string[i] 
        elif i % (int(max_width)) == 0:
            new_string = new_string +'\n'+ string[i]
        else:
            new_string = new_string + string[i]
    return new_string

if __name__ == '__main__':
    string = input("Input the paragraph here: ")
    max_width = input("max width of the line: ")
    new_string_line = wrap(string, max_width)
    print(new_string_line)