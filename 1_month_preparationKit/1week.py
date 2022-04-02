
def timeConversion(s):
    # Write your code here
    time = s[0:2]
    am_pm = s[8:10]
    converted_time = 0

    if am_pm == 'PM':
        if int(time) == 12:
            converted_time = time
        else:
            converted_time = int(time) + 12
    elif am_pm == 'AM':
        if int(time) == 12:
            converted_time = int(time) - 12
        else:
            converted_time = time
    new_time = f"{converted_time}:{s[3:5]}:{s[6:8]}"
    return print(new_time)
if __name__ == '__main__':

    s = input()
    result = timeConversion(s)