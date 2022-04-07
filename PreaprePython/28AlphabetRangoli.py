def print_rangoli(size):
    # your code goes here
    alphabet=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]


    upper_line = f"-{alphabet[size-1]}-"
    upper_right= ""
    upper_left= "" 

    for j in range(1,2*size):
        if j < size:
                line = (2*(size-j)-1)*"-" + upper_line +(2*(size-j)-1)*"-"
                upper_line = upper_left+ "-" +(alphabet[size-j])+"-"+alphabet[size-j-1]+"-"+ (alphabet[size-j])+"-"+upper_right
                upper_right =(alphabet[size-j])+"-"+ upper_right
                upper_left = upper_left + "-" + (alphabet[size-j])
                print(line)
        elif j==size:
            middle_line = "a"
            for i in range(1, size):
                middle_line = alphabet[i] + "-"+ middle_line + "-" + alphabet[i]
            print(middle_line)
        else:
            middle_part = f"{alphabet[j-size]}"
            i=2
            for k in range(1, (2*size-j)):
                middle_part = alphabet[j-size+k] +"-" + middle_part  +"-" + alphabet[j-size+k]
                i=i+1
            line = (2*(j-size))*"-" +middle_part +(2*(j-size))*"-"
            print(line)
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)

