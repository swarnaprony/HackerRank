def merge_the_tools(string, k):
    length = k
    substring = ""
    final_substring = ""
    for i in string:
        if len(substring) < k:
            substring += i
            if i not in final_substring:
                final_substring += i
        else:
            print(final_substring)
            substring = ""+i
            final_substring = ""+i
    print(final_substring)



if __name__ == '__main__':
    string = input("Input the string here: ")
    substring_length = int(input("Input length of substring here: "))
    merge_the_tools(string, substring_length)