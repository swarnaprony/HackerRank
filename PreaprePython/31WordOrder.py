
def order_words(words):
    word_list = {}
    word_number = []
    distinct_word = 0
    splited_word = words
    for word in splited_word:
        if word in word_list.keys():
            word_list[word].append(word)
        else:
            distinct_word += 1
            word_list[word] = [word]
    print(distinct_word)

    for i in word_list.keys():
        word_number.append(len(word_list.get(i)))
    print(*word_number, sep=' ')
    print(word_list)


if __name__ == '__main__':
    number = int(input())
    i = 0
    words = []
    while i < number:
        word = input()
        words.append(word)
        i = i+1
    order_words(words)

