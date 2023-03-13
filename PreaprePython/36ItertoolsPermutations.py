from itertools import permutations

def itertools_permutation(string, size):
    iter_list = list(permutations(string, int(size)))
    word = ''
    for i in iter_list:
        word = word.join(i)
        print(word)
        word = ''
    return

if __name__ == '__main__':
    itterative = input().split()
    itertools_permutation(sorted(itterative[0]), itterative[1])