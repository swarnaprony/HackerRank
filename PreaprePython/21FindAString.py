def count_substring(string, sub_string):
    count = 0
    for i in range(0, len(string)-len(sub_string)+1):
        if is_equal(string, sub_string, i) == True:
            count = count +1
    return count

def is_equal(string, sub_string, index):
    for j in range(0, len(sub_string)):
            if sub_string[j] != string[index+j]:
                return False
    return True

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)


