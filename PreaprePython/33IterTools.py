def iter_tools(a, b):
    lists = []
    tuple = ()
    tuples = ""
    for i in a:
        for j in b:
            tuples = tuples +  "(" + i + ", " + j + ")" + " "
    tuples = tuples[:-1]
    return print(tuples)



if __name__ == '__main__':
    i = 0
    a = 0 
    list = []
    while i <= 1:
        a = input()
        a = a.split()
        list.append(a)
        i = i+1

    iter_tools(list[0], list[1])
