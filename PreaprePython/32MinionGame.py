def minion_game(string):
    vowels = "AEIOU"
    stuart_word = ""
    kevin_word = ""
    stuart = []
    kevin = []
    kevin_points = 0
    stuarts_points = 0

    print("Length of the string: ", len(string))
    
    for i in range(len(string)):
        if string[i] in vowels:
            if kevin_word not in kevin:
                kevin_word = string[i]
                print(kevin_word)
                kevin.append(kevin_word)
                kevin_points = kevin_points + 1
                for j in range(i+1, len(string)):
                    if 
                    kevin_word = kevin_word + string[j]
                    if kevin_word not in kevin:
                        kevin.append(kevin_word)
                    kevin_points = kevin_points + 1
    
    print(kevin)
    print(kevin_points)

    return kevin




if __name__ == '__main__':
    s = input()
    minion_game(s)